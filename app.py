import streamlit as st
import joblib
from scipy.sparse import hstack
import numpy as np


clf_bundle = joblib.load("trainedmodels/classification_model.joblib")
reg_bundle = joblib.load("trainedmodels/regression_model.joblib")

clf_model = clf_bundle["model"]
reg_model = reg_bundle["model"]
tfidf = clf_bundle["tfidf"]  


math_symbols = ['$', '<', '>', '=', '+', '-', '*', '/', '^']

def extract_features(full_text):
    full_text = full_text.strip()

    text_length = len(full_text)
    math_count = sum(full_text.count(sym) for sym in math_symbols)

    X_text = tfidf.transform([full_text])
    X_numeric = np.array([[text_length, math_count]])

    return hstack([X_text, X_numeric])


st.set_page_config(page_title="AutoJudge", layout="centered")

st.title("AutoJudge")
st.subheader("Programming Problem Difficulty Predictor")

st.markdown(
    """
Enter the problem details below.  
The difficulty **class** and **score** are predicted independently.
"""
)

title = st.text_input("Problem Title")

description = st.text_area(
    "Problem Description",
    height=200
)

input_desc = st.text_area(
    "Input Description",
    height=120
)

output_desc = st.text_area(
    "Output Description",
    height=120
)

if st.button("Predict Difficulty"):
    full_text = " ".join([
        title,
        description,
        input_desc,
        output_desc
    ]).strip()

    if len(full_text) < 50:
        st.warning("No Problem Provided.")
    else:
        X = extract_features(full_text)

        predicted_class = clf_model.predict(X)[0]
        predicted_score = reg_model.predict(X)[0]

        predicted_score = max(1.0, min(10.0, predicted_score))
        predicted_score = round(predicted_score, 2)

        st.success("Prediction Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Predicted Difficulty Class", predicted_class)

        with col2:
            st.metric("Predicted Difficulty Score", predicted_score)

