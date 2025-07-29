from transformers import pipeline
from app.utils import clean_text

# Load once globally
classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news")

def detect_fake_review(text):
    cleaned = clean_text(text)
    result = classifier(cleaned)[0]
    label = "fake" if result["label"] == "LABEL_1" else "genuine"
    return label, result["score"]
