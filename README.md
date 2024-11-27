# CarDheko Used Car Price Prediction

This project predicts used car prices based on various features such as brand, type, mileage, kilometers driven, and more. It employs a Random Forest Regressor model and delivers predictions through a user-friendly Streamlit web application.

## Table of Contents
1. [Overview](#1-overview)  
2. [Directory Structure](#2-directory-structure)  
3. [Data Cleaning and Preprocessing](#3-data-cleaning-and-preprocessing)  
4. [Exploratory Data Analysis (EDA)](#4-exploratory-data-analysis-eda)  
5. [Machine Learning Model Development](#5-machine-learning-model-development)  
6. [Streamlit Application Development](#6-streamlit-application-development)  
7. [Requirements](#7-requirements)  
8. [Results](#8-results)  
9. [Conclusion](#9-conclusion)  

---

## 1. Overview
The project workflow includes:
- Cleaning and preprocessing car price data.  
- Performing exploratory data analysis to gain insights.  
- Developing a machine learning model for predicting car prices.  
- Deploying the model through a Streamlit-based web application for user-friendly interaction.  

---

## 2. Directory Structure
Car Price Prediction/ │ ├── CarDheko_ML.ipynb # Notebook for machine learning model development ├── CarDheko_processing.ipynb # Notebook for data preprocessing and cleaning ├── Streamlit.py # Streamlit app for car price prediction ├── cleaned_data.csv # Cleaned dataset ├── encoded_dataP.pkl # Encoded data in pickle format ├── processed_car_data.csv # Processed data used for modeling ├── random_forest_model.zip # Trained Random Forest model

---

## 3. Data Cleaning and Preprocessing
**Steps Followed:**
1. **Data Collection:**  
   - Collected data from various sources and stored it in a DataFrame.

2. **Handling Missing Data:**  
   - Identified and handled missing/null values using imputation or removal techniques.

3. **Feature Engineering:**  
   - Derived new features like `car_age`, `total_fuel_used`, and `price_per_km`.  
   - Removed highly correlated or unnecessary features to improve model efficiency.

4. **Encoding Categorical Variables:**  
   - Used `LabelEncoder` to convert categorical variables into numerical formats (e.g., `Body_Type`, `Fuel_Type`, `Transmission`).

5. **Log Transformation:**  
   - Applied log transformation to skewed numerical features like `price_per_km` and `total_fuel_used` for better prediction performance.

6. **Data Inspection:**  
   - Inspected feature structures, distributions, and relationships using visualizations.

---

## 4. Exploratory Data Analysis (EDA)
- Analyzed feature distributions and relationships.  
- Identified key trends and correlations using visual tools like histograms, scatter plots, and heatmaps.

---

## 5. Machine Learning Model Development
**Steps Followed:**
1. **Model Selection:**  
   - Chose Random Forest Regressor due to its ability to handle non-linear data and robust predictions.

2. **Model Training:**  
   - Split the dataset into training and testing sets.  
   - Trained the Random Forest Regressor on the training data.

3. **Model Evaluation:**  
   - Evaluated performance using 5-fold cross-validation, R² score, and RMSE.  

**Results:**  
- **R² Score:** 0.977 (explains 97.7% variance in car prices).  
- **RMSE:** ₹73,591 (average magnitude of prediction error).

---

## 6. Streamlit Application Development
**Steps Followed:**
1. **Streamlit Setup:**  
   - Developed an interactive web app using Streamlit.

2. **User Input:**  
   - Allowed users to input car details (e.g., `Body_Type`, `Kilometers_Driven`, `Engine_CC`, etc.) through a sidebar.  
   - Applied transformations (e.g., encoding categorical features) to make inputs compatible with the trained model.

3. **Prediction Display:**  
   - Displayed predicted car price when users clicked the **Predict Price** button.

---

## 7. Requirements
Ensure the following Python packages are installed:
- `pandas`  
- `scikit-learn`  
- `numpy`  
- `matplotlib`  
- `seaborn`  
- `streamlit`

---

## 8. Results
The Random Forest Regressor achieved the following:  
- **R² Score:** 0.977  
- **RMSE:** ₹73,591  

These metrics demonstrate the model’s reliability in predicting car prices based on the given features.

---

## 9. Conclusion
This project successfully predicts car prices using machine learning techniques, achieving high accuracy with the Random Forest Regressor. The Streamlit application makes predictions accessible through an intuitive interface.

