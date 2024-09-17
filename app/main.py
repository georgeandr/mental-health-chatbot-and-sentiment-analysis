from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["statement"]
        
        # Send the input to FastAPI for prediction
        response = requests.post("http://127.0.0.1:8000/predict", json={"cleaned_statement": user_input})
        
        # Get the prediction from FastAPI response
        prediction = response.json().get("prediction", "Error")
        
        return render_template("index.html", user_input=user_input, prediction=prediction)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
