import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model and encoded data
def load_model():
    return joblib.load(r'C:\Users\ramya\PycharmProjects\pythonProject1\Cardheko\random_forest_model.pkl')

def load_encoded_data():
    return joblib.load(r'C:\Users\ramya\PycharmProjects\pythonProject1\Cardheko\encoded_dataP.pkl')

# Main app
def main():
    st.title("Car Price Prediction App 🚗💰")
    st.write("This app predicts car prices based on your input!")

    # Load resources
    model = load_model()
    encoded_data = load_encoded_data()

    # Features used for price prediction
    feature_columns = [
        'Body_Type', 'Kilometers_Driven', 'Owner_Count', 'oem', 'Fuel_Type', 'Transmission',
        'Engine_CC', 'Height_mm', 'Kerb_weight_kg', 'Tyre_Type', 'Mileage_Kmpl', 'Torque_Nm',
        'Seats', 'Wheel_size', 'City','car_age', 'price_per_km'
    ]

    # Create a reverse dictionary to map encoded values back to original labels for Body_Type, Fuel_Type, etc.
    body_type_mapping = { 0: 'Convertibles', 1: 'Coupe', 2: 'Hatchback', 3: 'Hybrids', 4: 'MUV',
                          5: 'Minivans', 6: 'Pickup Trucks', 7: 'SUV', 8: 'Sedan', 9: 'Wagon' }
    oem_mapping = { 0: 'Audi', 1: 'BMW', 2: 'Chevrolet', 3: 'Citroen', 4: 'Datsun', 5: 'Fiat',
                    6: 'Ford', 7: 'Hindustan Motors', 8: 'Honda', 9: 'Hyundai', 10: 'Isuzu', 11: 'Jaguar',
                    12: 'Jeep', 13: 'Kia', 14: 'Land Rover', 15: 'Lexus', 16: 'MG', 17: 'Mahindra',
                    18: 'Mahindra Renault', 19: 'Mahindra Ssangyong', 20: 'Maruti', 21: 'Mercedes-Benz',
                    22: 'Mini', 23: 'Mitsubishi', 24: 'Nissan', 25: 'Opel', 26: 'Porsche', 27: 'Renault',
                    28: 'Skoda', 29: 'Tata', 30: 'Toyota', 31: 'Volkswagen', 32: 'Volvo' }
    fuel_type_mapping = { 0: 'CNG', 1: 'Diesel', 2: 'Electric', 3: 'LPG', 4: 'Petrol' }
    transmission_mapping = { 0: 'Manual', 1: 'Automatic' }
    tyre_type_mapping = { 0: 'AllTerrain', 1: 'MudTerrain', 2: 'Radial', 3: 'Runflat',
                          4: 'RunflatRadial', 5: 'Tubeless', 6: 'Tubeless Tyre', 7: 'TubelessRadial',
                          8: 'TubelessRunflat' }
    city_mapping = { 0: 'Bangalore', 1: 'Chennai', 2: 'Delhi', 3: 'Hyderabad', 4: 'Jaipur', 5: 'Kolkata' }

    # Sidebar for user input
    st.sidebar.header("Enter Car Details")
    user_input = {}

    # Create input fields for the user based on the selected features
    for col in feature_columns:
        if col in ['Kilometers_Driven', 'Engine_CC', 'Mileage_Kmpl', 'Torque_Nm', 'Seats', 'Height_mm',
                   'Kerb_weight_kg', 'Wheel_size', 'car_age', 'price_per_km']:
            if col == 'Kilometers_Driven':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=0.0, value=120000.0, step=100.0)
            elif col == 'Engine_CC':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=0.0, value=998.0, step=100.0)
            elif col == 'Mileage_Kmpl':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=5.0, value=23.1, step=0.1)
            elif col == 'Torque_Nm':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=4.0, value=90.0, step=1.0)
            elif col == 'Seats':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=2.0, value=5.0, step=1.0)
            elif col == 'Height_mm':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=1000.0, value=1565.0, step=10.0)
            elif col == 'Kerb_weight_kg':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=500.0, value=835.0, step=50.0)
            elif col == 'Wheel_size':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=10.0, value=15.7, step=1.0)
            elif col == 'car_age':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=1.0, value=9.0, step=1.0)
            elif col == 'price_per_km':
                user_input[col] = st.sidebar.number_input(f"{col}", min_value=0.2, value=1.5, step=0.1)

        elif col in ['Body_Type', 'oem', 'Fuel_Type', 'Transmission', 'Tyre_Type', 'City']:
            if col == 'Body_Type':
                options = list(body_type_mapping.values())  # Use original body type labels
                user_input[col] = st.sidebar.selectbox(f"{col}", options)
            elif col == 'oem':
                options = list(oem_mapping.values())  # Use original model type labels
                user_input[col] = st.sidebar.selectbox(f"{col}", options)
            elif col == 'Fuel_Type':
                options = list(fuel_type_mapping.values())  # Use original fuel type labels
                user_input[col] = st.sidebar.selectbox(f"{col}", options)
            elif col == 'Transmission':
                options = list(transmission_mapping.values())  # Use original Transmission type labels
                user_input[col] = st.sidebar.selectbox(f"{col}", options)
            elif col == 'Tyre_Type':
                options = list(tyre_type_mapping.values())  # Use original tyre type labels
                user_input[col] = st.sidebar.selectbox(f"{col}", options)
            elif col == 'City':
                options = list(city_mapping.values())  # Use original City type labels
                user_input[col] = st.sidebar.selectbox(f"{col}", options)
        else:
            user_input[col] = st.sidebar.number_input(f"{col}", value=0)

    # Convert user input to DataFrame for prediction
    user_input_df = pd.DataFrame([user_input])

    # Encode categorical features using LabelEncoder (Apply same encoding as during training)
    user_input_df_encoded = user_input_df.copy()

    # Apply the reverse encoding (encoding similar to training)
    for col in ['Body_Type', 'oem', 'Fuel_Type', 'Transmission', 'Tyre_Type', 'City']:
        if col == 'Body_Type':
            user_input_df_encoded[col] = user_input_df[col].map(body_type_mapping)
        elif col == 'oem':
            user_input_df_encoded[col] = user_input_df[col].map(oem_mapping)
        elif col == 'Fuel_Type':
            user_input_df_encoded[col] = user_input_df[col].map(fuel_type_mapping)
        elif col == 'Transmission':
            user_input_df_encoded[col] = user_input_df[col].map(transmission_mapping)
        elif col == 'Tyre_Type':
            user_input_df_encoded[col] = user_input_df[col].map(tyre_type_mapping)
        elif col == 'City':
            user_input_df_encoded[col] = user_input_df[col].map(city_mapping)

    # Predict price
    if st.sidebar.button("Predict Price"):
        prediction = model.predict(user_input_df_encoded)
        st.subheader("Predicted Price")
        st.write(f"₹ {prediction[0]:,.2f}")  # No need for inverse log transformation here


if __name__ == "__main__":
    main()
