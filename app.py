import streamlit as st
from fuzzywuzzy import fuzz

def compute_similarity_scores(q1, q2):
    scores = {
        "Overall Ratio": fuzz.QRatio(q1, q2),
        "Partial Ratio": fuzz.partial_ratio(q1, q2),
        "Token Sort Ratio": fuzz.token_sort_ratio(q1, q2),
        "Token Set Ratio": fuzz.token_set_ratio(q1, q2)
    }
    return scores

def predict_similarity(scores, threshold=70):
    weights = {
        "Overall Ratio": 0.2,
        "Partial Ratio": 0.3,
        "Token Sort Ratio": 0.25,
        "Token Set Ratio": 0.25
    }
    
    weighted_score = sum(scores[k] * weights[k] for k in scores) / sum(weights.values())
    is_duplicate = weighted_score >= threshold
    
    if is_duplicate:
        return "Duplicate"
    else:
        return "Not Duplicate"

st.title("Question Similarity Checker")
q1 = st.text_input("Enter first question:")
q2 = st.text_input("Enter second question:")

if st.button("Check Similarity"):
    if not q1 or not q2:
        st.warning("Please enter both questions.")
    else:
        # Calculate similarity scores
        scores = compute_similarity_scores(q1, q2)
        
        # Make prediction based on scores
        result = predict_similarity(scores)
        
        # Display only the simplified prediction
        st.write("### Simplified Prediction:")
        st.write(f"**{result}**")
