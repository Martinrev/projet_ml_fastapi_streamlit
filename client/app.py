import streamlit as st
import requests

st.title("modèle Random forest sur données iris ")

sepal_length = st.slider("Sepal Length:", 0.0, 10.0)
sepal_width = st.slider("Sepal Width:", 0.0, 10.0)
petal_length = st.slider("Petal Length:", 0.0, 10.0)
petal_width = st.slider("Petal Width:", 0.0, 10.0)

if st.button("Predict"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
    }

    response = requests.post("http://server:8000/predict", json=data)

    if response.status_code == 200:
        prediction = response.json()["predicted_class"]
        st.success(f"Predicted Class: {prediction}")
    else:
        st.error(f"Error: {response.text}")