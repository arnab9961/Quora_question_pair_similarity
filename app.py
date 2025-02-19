import streamlit as st
import pickle
import numpy as np
from fuzzywuzzy import fuzz

def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def compute_features(q1, q2):
    features = [
        fuzz.QRatio(q1, q2),
        fuzz.partial_ratio(q1, q2),
        fuzz.token_sort_ratio(q1, q2),
        fuzz.token_set_ratio(q1, q2)
    ]
    return np.array(features).reshape(1, -1)

st.title("Question Similarity Checker")

q1 = st.text_input("Enter first question:")
q2 = st.text_input("Enter second question:")

if st.button("Check Similarity"):
    if not q1 or not q2:
        st.warning("Please enter both questions.")
    else:
        model = load_model()
        features = compute_features(q1, q2)
        prediction = model.predict(features)[0]
        result = "Duplicate" if prediction == 1 else "Not Duplicate"
        st.write(f"### Prediction: {result}")
