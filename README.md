<h1 align="center" id="title">Mental Health Chatbot and Sentiment Analysis</h1>

<p id="description">This project aims to provide hands-on experience with various technologies such as Flask FastAPI and deploying a machine learning model into production. The main goal was not to optimize the machine learning model's performance but to focus on the end-to-end development process including building a web interface handling API requests and deploying an ML model.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Front-end: A simple web interface using HTML and CSS for users to input data.
*   Back-end: A Flask app to serve the front-end and a FastAPI service to handle the machine learning prediction.
*   Machine Learning: A sentiment analysis model using Random Forest trained on mental health-related data.

<br><b>Note:</b>  The model is used for demonstration purposes and was not optimized for performance.

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository</p>

```
git clone https://github.com/georgeandr/mental-health-chatbot-and-sentiment-analysis.git
```

<p>2. Set up the virtual environment</p>

```
python3 -m venv venv 
source venv/bin/activate 
pip install -r requirements.txt
```

<p>3. Run the FastAPI backend</p>

```
cd api 
uvicorn main:app --reload
```

<p>4. Run the Flask based front-end app</p>

```
cd app
python3 main.py
```

<p>5. Access the front-end at</p>

```
http://127.0.0.1:5000
```

<p>6. Input a custom text to the sentiment prediction</p>

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   FastAPI
*   Flask
*   Python

<h2>Future Improvements</h2>

* Model Optimization: The current machine learning model can be optimized for better performance.
* Testing and Validation: More rigorous testing of both the API and the machine learning model.
* Additional Features: Implement more robust front-end features and user authentication.