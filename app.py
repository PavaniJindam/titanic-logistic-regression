
import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("titanic_model.pkl")

st.title("Titanic Survival Prediction")
st.write("Enter passenger details to predict the survival outcome.")

# User inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["female", "male"])
age = st.number_input("Age", min_value=0.0, max_value=100.0, value=25.0)
sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("Ticket Fare", min_value=0.0, value=32.0)
embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

# Predict survival
if st.button("Predict Survival"):
    passenger = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked": embarked
    }])

    prediction = model.predict(passenger)[0]

    if prediction == 1:
        st.success("Prediction: Passenger Survived")
    else:
        st.error("Prediction: Passenger Did Not Survive")
