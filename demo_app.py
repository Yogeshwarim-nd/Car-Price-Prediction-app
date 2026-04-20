import streamlit as st
import pandas as pd
import pickle


def load_model():
    with open("xgb_car_price_model.pkl",'rb') as f:
        model=pickle.load(f)
    return model

st.header("Car Price Prediction")
st.write("Enter the Car details to predict the price.")

km_driven=st.number_input("KM Driven",min_value=0,max_value=1000000,value=50000)
mileage =  st.number_input("Mileage", min_value=2, max_value=100,value=15)
age = st.number_input("Age", min_value=0, max_value=20,value=5)
fuel_type=st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])

fuel_encoding = {
    "Petrol": [1, 0, 0],
    "Diesel": [0, 1, 0],
    "Electric": [0, 0, 1]}


petrol, diesel, electric = fuel_encoding[fuel_type]


input_df = pd.DataFrame([[km_driven, mileage, age, petrol, diesel, electric]],
                        columns=['km_driven','mileage','age','Petrol','Diesel','Electric'])
# input_df = input_df.reset_index(drop=True)



st.dataframe(input_df)

if st.button("Predict price"):
    model=load_model()
    prediction = model.predict(input_df)[0]
    st.write(f"The predicted selling price is: ₹ {prediction:,.2f}")
