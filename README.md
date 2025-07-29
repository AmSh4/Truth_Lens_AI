# TruthLensAI – Multimodal Fake Review Detection System 🕵️‍♂️💬

##  Overview
**TruthLensAI** is an advanced AI/ML web app that detects fake reviews by analyzing:
-  Textual content (BERT fine-tuned)
-  Product images (CNN-based image validation)
-  Sentiment polarity
-  Historical reviewer behavior via MongoDB

##  Tech Stack
- **Python**, **Transformers (HuggingFace)**, **PyTorch**, **Streamlit**
- **CNN for image classification**
- **MongoDB** for user-review data tracking
- **Matplotlib**, **Seaborn**, **NLTK**, **Scikit-learn**

##  Features
- Analyze review **text and image** together
- Detect review **authenticity**
- Generate **confidence score** for every review
- Visualize insights with real-time graphs
- Lightweight **Streamlit GUI**

## Folder Structure:
      TruthLensAI/
      │
      ├── app/                          # Streamlit front-end
      │   ├── main.py
      │   └── utils.py
      │
      ├── backend/
      │   ├── fake_review_detector.py  # ML model pipeline
      │   ├── sentiment_analysis.py
      │   ├── image_validator.py       # Computer vision module
      │   └── model_loader.py
      │
      ├── data/
      │   ├── reviews.csv              # Sample fake/genuine reviews
      │   └── product_images/
      │       └── *.jpg
      │
      ├── models/
      │   ├── bert_finetuned.pth
      │   └── cnn_image_classifier.pth
      │
      ├── database/
      │   ├── db_utils.py              # MongoDB interaction
      │   └── schema.json
      │
      ├── tests/
      │   └── test_pipeline.py         # Unit tests
      │
      ├── README.md
      ├── requirements.txt



## Dataset
- `reviews.csv`: 3000+ reviews (fake/genuine) scraped from Amazon, Yelp, TripAdvisor
- `product_images/`: 200+ product images

## Setup Instructions
```bash
git clone https://github.com/AmSh4/TruthLensAI
cd TruthLensAI
pip install -r requirements.txt
streamlit run app/main.py
```

## Model Info
- BERT fine-tuned on custom fake review dataset
- CNN trained on synthetic vs real product image datasets


