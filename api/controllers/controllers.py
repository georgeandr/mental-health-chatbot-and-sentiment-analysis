from fastapi import APIRouter
from helpers.functions import preprocess_text
from constants.constants import TextData
import joblib

router = APIRouter()

# Load the saved model and vectorizer
rf_model = joblib.load('../models/random_forest_model.pkl')
vectorizer = joblib.load('../models/tfidf_vectorizer.pkl')

# Prediction endpoint
@router.post("/predict")
def predict_sentiment(data: TextData):
    # Preprocess the input text
    input_processed = preprocess_text(data.cleaned_statement)
    
    # Vectorize the input
    input_vectorized = vectorizer.transform([input_processed])
    
    # Make the prediction
    prediction = rf_model.predict(input_vectorized)
    
    return {'prediction': prediction[0]}
