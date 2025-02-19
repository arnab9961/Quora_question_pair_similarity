import streamlit as st
import pickle
import numpy as np
from thefuzz import fuzz
import os

# Set Page Title with Search Icon in Tab
st.set_page_config(
    page_title="🔍 Question Similarity Checker",  # Added search icon in the title
    layout="centered"
)

def load_model():
    try:
        model_path = "model.pkl"
        if not os.path.exists(model_path):
            return None
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    except Exception:
        return None

def compute_features(q1, q2):
    features = [
        fuzz.QRatio(q1, q2),
        fuzz.partial_ratio(q1, q2),
        fuzz.token_sort_ratio(q1, q2),
        fuzz.token_set_ratio(q1, q2)
    ]
    return np.array(features).reshape(1, -1)

# Apply Gradient Background & White Box Styling
custom_css = """
<style>
    /* Gradient Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #FF9A8B, #FF6A88, #FF99AC);
    }
    
    /* White Box */
    .white-box {
        background: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        max-width: 600px;
        margin: auto;
        text-align: center;
    }

    /* Title Styling */
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    .title span {
        color: red;
        font-size: 60px;
    }

    /* Prediction Box */
    .prediction-box {
        font-size: 28px; 
        font-weight: bold; 
        padding: 20px; 
        border-radius: 8px; 
        text-align: center;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# White Box Wrapper
st.markdown('<div class="white-box">', unsafe_allow_html=True)

# Title
st.markdown('<div class="title"><span>Q</span>uestion Similarity Checker</div>', unsafe_allow_html=True)
st.write("🔍 Check if two questions are duplicates.")

# Input Fields
q1 = st.text_input("Enter first question:")
q2 = st.text_input("Enter second question:")

# Button
if st.button("🔎 Check Similarity"):
    if not q1 or not q2:
        st.warning("⚠️ Please enter both questions.")
    else:
        model = load_model()
        if model is not None:
            try:
                features = compute_features(q1, q2)
                prediction = model.predict(features)[0]
                result = "✅ Duplicate" if prediction == 1 else "❌ Not Duplicate"
            except:
                result = "⚠️ Error in model prediction"
        else:
            avg_score = sum([
                fuzz.QRatio(q1, q2),
                fuzz.partial_ratio(q1, q2),
                fuzz.token_sort_ratio(q1, q2),
                fuzz.token_set_ratio(q1, q2)
            ]) / 4
            result = "✅ Duplicate" if avg_score > 70 else "❌ Not Duplicate"

        st.markdown(f'<div class="prediction-box">{result}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close the white-box div
