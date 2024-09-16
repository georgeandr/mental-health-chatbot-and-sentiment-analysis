from functions import preprocess_text
import joblib

def main():
    rf_model = joblib.load("../mental-health-chatbot-and-sentiment-analysis/models/random_forest_model.pkl")
    vectorizer = joblib.load("../mental-health-chatbot-and-sentiment-analysis/models/tfidf_vectorizer.pkl")

    custom_input = "I feel very happy and excited today!"
    input_processed = preprocess_text(custom_input)

    custom_input_vectorized = vectorizer.transform([input_processed])
    predict_label = rf_model.predict(custom_input_vectorized)
    return print(predict_label)

if __name__ == "__main__":
    main()