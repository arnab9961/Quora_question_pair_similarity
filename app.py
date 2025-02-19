import streamlit as st
import pickle
import numpy as np
from thefuzz import fuzz
import os

st.set_page_config(page_title="Question Similarity Checker", layout="centered")

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

# UI Styling
custom_css = """
<style>
    body { background-color: #121212; color: #ffffff; font-family: 'Arial', sans-serif; }
    .main { background-color: #1E1E1E; padding: 30px; border-radius: 10px; }
    input, textarea { background-color: #333; color: #fff; border-radius: 5px; }
    button { background-color: #FF4B4B; color: white; font-size: 18px; padding: 10px; border-radius: 5px; border: none; }
    button:hover { background-color: #FF2222; }
    .prediction-box { font-size: 24px; font-weight: bold; padding: 20px; border-radius: 8px; text-align: center; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Try to Load Image
image_path = "transparent_image.png"
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.write("🔹 **Upload a transparent background image for a better UI!**")

st.title("🚀 Question Similarity Checker")
st.write("🔍 Check if two questions are duplicates.")

q1 = st.text_input("Enter first question:")
q2 = st.text_input("Enter second question:")

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
