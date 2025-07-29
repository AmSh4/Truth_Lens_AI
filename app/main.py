import streamlit as st
from backend.fake_review_detector import detect_fake_review
from backend.sentiment_analysis import analyze_sentiment
from backend.image_validator import validate_image
from PIL import Image
import os

st.set_page_config(page_title="TruthLensAI", layout="wide")
st.title("🕵️ TruthLensAI – Fake Review Detection System")

review = st.text_area("✍️ Enter Review Text", height=150)
uploaded_image = st.file_uploader("📷 Upload Product Image", type=["jpg", "png", "jpeg"])

if st.button("Analyze"):
    if review:
        label, confidence = detect_fake_review(review)
        sentiment = analyze_sentiment(review)
        st.subheader(f"🔍 Review Analysis: {label.upper()} ({confidence*100:.2f}%)")
        st.write(f"🧠 Sentiment: {sentiment}")

    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        prediction = validate_image(img)
        st.write(f"🖼️ Image Validation: {prediction}")
