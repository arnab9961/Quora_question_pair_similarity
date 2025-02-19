import streamlit as st
import pickle
import numpy as np
from fuzzywuzzy import fuzz
import os

def load_model():
    try:
        model_path = "model.pkl"
        if not os.path.exists(model_path):
            st.error(f"Model file not found at {model_path}. Please check file location.")
            return None
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def compute_features(q1, q2):
    features = [
        fuzz.QRatio(q1, q2),
        fuzz.partial_ratio(q1, q2),
        fuzz.token_sort_ratio(q1, q2),
        fuzz.token_set_ratio(q1, q2)
    ]
    return np.array(features).reshape(1, -1)

def compute_similarity_scores(q1, q2):
    scores = {
        "Overall Ratio": fuzz.QRatio(q1, q2),
        "Partial Ratio": fuzz.partial_ratio(q1, q2),
        "Token Sort Ratio": fuzz.token_sort_ratio(q1, q2),
        "Token Set Ratio": fuzz.token_set_ratio(q1, q2)
    }
    return scores

st.title("Question Similarity Checker")
st.write("Check if two questions are duplicates of each other.")

q1 = st.text_input("Enter first question:")
q2 = st.text_input("Enter second question:")

if st.button("Check Similarity"):
    if not q1 or not q2:
        st.warning("Please enter both questions.")
    else:
        # Display similarity scores
        scores = compute_similarity_scores(q1, q2)
        st.write("### Similarity Scores:")
        for metric, score in scores.items():
            st.write(f"**{metric}**: {score}%")

        # Load model and make prediction if available
        model = load_model()
        if model is not None:
            try:
                features = compute_features(q1, q2)
                prediction = model.predict(features)[0]
                result = "Duplicate" if prediction == 1 else "Not Duplicate"
                st.write(f"### Model Prediction: {result}")
            except Exception as e:
                st.error(f"Error making prediction: {str(e)}")

        # Simplified fallback prediction
        avg_score = sum(scores.values()) / len(scores)
        fallback_result = "Duplicate" if avg_score > 70 else "Not Duplicate"
        st.write(f"### Prediction: {fallback_result}")
