from flask import Flask, request
from transformers import pipeline

# Allocate a pipeline for sentiment-analysis
nlp = pipeline('sentiment-analysis')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/sentiment', methods=['POST'])
def sentiment():
    # Get the text from the POST request
    text = request.json.get('text', 'I love transformers!')

    # Perform sentiment analysis
    result = nlp(text)

    # Return the result as JSON
    return {'result': result}
