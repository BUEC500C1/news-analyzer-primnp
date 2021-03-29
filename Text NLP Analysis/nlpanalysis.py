from flask import Flask, redirect, url_for, jsonify
from flask_restful import Resource, Api
import json
import sys
import os
import nlpanalysis_calc as nlp


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return redirect(url_for('nlp_home'))

# home page
@app.route('/nlp')
def nlp_home():
    return '''
        <h1>Text NLP Analysis</h1>
        <p>Please review documentation for testing</p>
    '''

# retrieve sentiment of the text
@app.route('/nlp/retrieve-sentiment/<text>')
def analyze_sentiment(text):
    results = []
    res = dict()
    res["SentimentScore"] = nlp.returnSentiment(text)
    res["TextInput"] = text
    results.append(res)
    return jsonify(results)

# retrieve entities of the text
@app.route('/nlp/retrieve-entity/<text>')
def analyze_entities(text):
    results = []
    res = dict()
    res["Entities"] = nlp.returnEntities(text)
    res["TextInput"] = text
    results.append(res)
    return jsonify(results)

# retrieve entities and sentiments of the text
@app.route('/nlp/retrieve-entity-sentiment/<text>')
def analyze_entities_sentiments(text):
    # results = []
    res = dict()
    res["Results"] = nlp.returnEntitiesAndSentiments(text)
    # res["TextInput"] = text
    # results.append(res)
    return res

# classify text's possible categories
@app.route('/nlp/content-classification/<text>')
def classify_content(text):
    # results = []
    res = dict()
    res["Results"] = nlp.classifyContent(text)
    # res["TextInput"] = text
    # results.append(res)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
