from fastapi import APIRouter
from constants.constants import TextData
import controllers.controllers as controllers

router = APIRouter()

# Prediction endpoint
@router.post("/predict")
def predict_sentiment(data: TextData):
    return controllers.predict_sentiment(data)
