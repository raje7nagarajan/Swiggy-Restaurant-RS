# Swiggy Restaurant Recommendation System

## Overview
This project builds a **restaurant recommendation system** using **Streamlit**. The system suggests restaurants based on user preferences such as **city, cuisine, rating, and cost**.

## Objective
- Build a recommendation system using **restaurant data** from a CSV file.
- Utilize **clustering** for recommendations.
- Display recommendations in an **interactive Streamlit interface**.

## Features
- Personalized restaurant recommendations
- Interactive Streamlit UI
- Clustering or similarity-based methodology
- Optimized filtering system

## Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Pickle**

## Project Files

- Swiggy_rs_Final.ipynb → This file would contain data exploration, preprocessing, model training, and evaluation steps
- SRS_app.py → The main Streamlit application for restaurant recommendations.

- cleaned_data.csv → The cleaned restaurant dataset after preprocessing.

- encoded_data.csv → The transformed dataset with encoded categorical values.

- kmeans_model.pkl → Trained K-Means clustering model for recommendations.

- encoder.pkl → One-Hot Encoder model for feature transformation.

## Approach

### Data Cleaning
- Remove duplicates.
- Handle missing values.
- Save cleaned data to `cleaned_data.csv`.

### Data Preprocessing
- Apply **One-Hot Encoding** to categorical features.
- Save **encoder model** as `encoder.pkl`.
- Ensure the dataset is fully numerical.

### Recommendation Methodology
- Use **K-Means Clustering**.
- Compute similarity using the **encoded dataset**.
- Map **recommendations** back to `cleaned_data.csv`.

### Streamlit Application
- Users input **city, cuisine, rating, and cost**.
- The recommendation engine suggests **top restaurants**.
- Results displayed dynamically using **Streamlit**.

**Note** The input file is not attached due to the size.
