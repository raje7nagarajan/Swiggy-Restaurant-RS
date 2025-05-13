# Required header file
import streamlit as st
import pandas as pd
import pickle

# Load restaurant dataset (non-encoded for display, encoded for clustering)
original_df = pd.read_csv("cleaned_data.csv")       # Data without encoding
encoded_df = pd.read_csv("encoded_data.csv")        # Encoded numerical data
encoded_df = encoded_df.select_dtypes(include=['number'])  # Select only numerical columns

# Load the pre-trained KMeans clustering model from a pickle file
with open("kmeans_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

# Assign clusters to restaurants if they are missing in the original dataset
if 'cluster' not in original_df.columns:
    encoded_df['cluster'] = kmeans.predict(encoded_df)  # Predict cluster labels
    original_df['cluster'] = encoded_df['cluster']  # Add clusters to the main dataset

# Title of the application with custom styling
st.markdown("<h3 style='color: #fc5a03; text-align: center; font-weight: bold;'>Swiggy Restaurant Recommendation System</h3>", unsafe_allow_html=True)

# Get unique cities and cuisines for user selection
cities = original_df['city'].dropna().unique()
cuisines = original_df['cuisine'].dropna().unique()

# Inject custom CSS to style the slider color (orange)
st.markdown(
    """
    <style>
    div[data-testid="stSlider"] div[role="slider"] {
        background-color: #fc5a03!important;  /* Orange slider color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# User selects a city from the dropdown list
st.markdown("<h4 style='color: #fc5a03;'>Select City</h4>", unsafe_allow_html=True)
city = st.selectbox("", sorted(cities))

# User selects preferred cuisines (multiple options)
st.markdown("<h4 style='color: #fc5a03;'>Preferred Cuisine(s)</h4>", unsafe_allow_html=True)
cuisine = st.multiselect("", sorted(cuisines))

# User selects the minimum rating for restaurants
st.markdown("<h4 style='color: #fc5a03;'>Minimum Rating</h4>", unsafe_allow_html=True)
min_rating = st.slider("Select Rating", 0.0, 5.0, 3.0)

# User selects the maximum price they are willing to pay
st.markdown("<h4 style='color: #fc5a03;'>Maximum Price</h4>", unsafe_allow_html=True)
max_price = st.slider("Select Price", 0, 1000, 500)

# Filter restaurants based on user input (city, rating, and cost)
filtered_df = original_df[
    (original_df['city'] == city) &
    (original_df['rating'] >= min_rating) &
    (original_df['cost'] <= max_price)
]

# If user has selected a cuisine, filter restaurants that match any selected cuisine
if cuisine:
    filtered_df = filtered_df[filtered_df['cuisine'].str.contains('|'.join(cuisine), case=False)]

# Display section for recommended restaurants
st.markdown("<h4 style='color: #fc5a03; text-align: center; font-weight: bold;'>Recommended Restaurants</h4>", unsafe_allow_html=True)

# If matching restaurants exist, recommend based on cluster similarity
if not filtered_df.empty:
    selected_index = filtered_df.index[0]  # First matching restaurant
    selected_cluster = original_df.loc[selected_index, 'cluster']  # Cluster it belongs to

    # Find other restaurants in the same cluster (excluding the selected restaurant)
    recommendations = original_df[
        (original_df['cluster'] == selected_cluster) &
        (original_df.index != selected_index)
    ].head(5)  # Limit recommendations to 5

    # Select key columns for display
    display_df = recommendations[['name', 'address', 'cuisine', 'rating', 'cost']].copy()
    display_df.columns = ['Name', 'Address', 'Cuisine', 'Rating', 'Cost (₹)']

    # Format rating to one decimal place, and cost with currency
    display_df['Rating'] = display_df['Rating'].map('{:.1f}'.format)
    display_df['Cost (₹)'] = display_df['Cost (₹)'].map('₹{:,.0f}'.format)

    # Display recommended restaurants in a table format
    st.dataframe(display_df)

else:
    st.warning("No restaurants found matching your criteria.")  # Show a warning if no matches
