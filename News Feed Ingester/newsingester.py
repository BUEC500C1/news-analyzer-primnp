from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_restful import Resource, Api
import sys
import os
import newsingester_calc as news

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return redirect(url_for('news_home'))

# home page
@app.route('/newsfeedig')
def news_home():
    return """
    <h1>News Feed Ingester</h1>
    <p>Please refer to readme.md on how to utilize this API</p>
    """

# query with one keyword
@app.route('/newsfeedig/onequery/<keyword>')
def one_query(keyword):
    res = dict()
    res['News Feed Results'] = news.findWithKeyword(keyword)
    return jsonify(res)

# query with several keywords separated by '-' when input
@app.route('/newsfeedig/listquery/<string:keywords>')
def list_query(keywords):
    keywords = keywords.split('-')
    res = dict()
    res['News Feed Results'] = news.findWithKeywordLists(keywords)
    return jsonify(res)

@app.route('/newsfeedig/dmyquery/year1=<string:year1>&month1=<string:month1>&day1=<string:day1>&year2=<string:year2>&month2=<string:month2>&day2=<string:day2>&keywords=<string:keywords>')
def dmy_query(year2, year1, month2, month1, day2, day1, keywords):
    keywords = keywords.split('-')
    res = dict()
    res['News Feed Results'] = news.findWithDMY(year2, year1, month2, month1, day2, day1, keywords)
    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
