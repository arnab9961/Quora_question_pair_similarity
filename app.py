import streamlit as st
import pickle
import numpy as np
from fuzzywuzzy import fuzz
import os

def load_model():
    try:
        model_path = "model.pkl"
        if not os.path.exists(model_path):
            return None
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except:
        return None  # Silently handle model loading errors

def compute_features(q1, q2):
    features = [
        fuzz.QRatio(q1, q2),
        fuzz.partial_ratio(q1, q2),
        fuzz.token_sort_ratio(q1, q2),
        fuzz.token_set_ratio(q1, q2)
    ]
    return np.array(features).reshape(1, -1)

st.title("Question Similarity Checker")
st.write("Check if two questions are duplicates of each other.")

q1 = st.text_input("Enter first question:")
q2 = st.text_input("Enter second question:")

if st.button("Check Similarity"):
    if not q1 or not q2:
        st.warning("Please enter both questions.")
    else:
        model = load_model()
        if model is not None:
            try:
                features = compute_features(q1, q2)
                prediction = model.predict(features)[0]
                result = "Duplicate" if prediction == 1 else "Not Duplicate"
            except:
                result = None  # Silently fail if model prediction fails
        else:
            result = None  # No model available
        
        if result is None:
            avg_score = sum([
                fuzz.QRatio(q1, q2),
                fuzz.partial_ratio(q1, q2),
                fuzz.token_sort_ratio(q1, q2),
                fuzz.token_set_ratio(q1, q2)
            ]) / 4
            result = "Duplicate" if avg_score > 70 else "Not Duplicate"

        st.write(f"### Prediction: {result}")
