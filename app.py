import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Set up the page
st.title("🏡 House Price Prediction App")
st.write("Enter the details of the house below to predict its price.")

# User input fields
squareMeters = st.number_input("Square Meters", min_value=10.0, step=1.0)
numberOfRooms = st.number_input("Number of Rooms", min_value=1, step=1)
hasYard = st.selectbox("Has Yard", [0, 1])
hasPool = st.selectbox("Has Pool", [0, 1])
floors = st.number_input("Number of Floors", min_value=1, step=1)
cityCode = st.number_input("City Code", min_value=1, step=1)
cityPartRange = st.number_input("City Part Range", min_value=1, step=1)
numPrevOwners = st.number_input("Number of Previous Owners", min_value=0, step=1)
made = st.number_input("Year Built (e.g., 2005)", min_value=1800, max_value=2025)
isNewBuilt = st.selectbox("Is New Built", [0, 1])
hasStormProtector = st.selectbox("Has Storm Protector", [0, 1])
basement = st.selectbox("Has Basement", [0, 1])
attic = st.selectbox("Has Attic", [0, 1])
garage = st.selectbox("Has Garage", [0, 1])
hasStorageRoom = st.selectbox("Has Storage Room", [0, 1])
hasGuestRoom = st.selectbox("Has Guest Room", [0, 1])

# Predict button
if st.button("Predict Price"):
    # Create input DataFrame
    input_data = pd.DataFrame([[squareMeters, numberOfRooms, hasYard, hasPool, floors, cityCode,
                                cityPartRange, numPrevOwners, made, isNewBuilt, hasStormProtector,
                                basement, attic, garage, hasStorageRoom, hasGuestRoom]],
                              columns=['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors',
                                       'cityCode', 'cityPartRange', 'numPrevOwners', 'made', 'isNewBuilt',
                                       'hasStormProtector', 'basement', 'attic', 'garage', 'hasStorageRoom',
                                       'hasGuestRoom'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show result
    st.success(f"💰 Estimated House Price: ${prediction:,.2f}")
