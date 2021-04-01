# based on https://developer.nytimes.com/docs/articlesearch-product/1/types/Article
from pynytimes import NYTAPI
import os
import json
import datetime
import logging

logging.basicConfig(filename='newsfeed.log', level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')

def nyt_api():
    nytkey = os.getenv("NYT_KEY")
    nyt = NYTAPI(str(nytkey), parse_dates=True)
    return nyt

# query with only one keyword (string input)
def findWithKeyword(keyword):
    logging.info('Start query with a keyword')
    nyt = nyt_api()

    if type(keyword) is str:
        results  = []
        articles = nyt.article_search(
            query=keyword,
            results=10,  #display 10 results
        )
        for article in articles:
            res = dict()
            res['WebURL'] = article.get('web_url')
            res['Snippet'] = article.get('snippet')
            res['Source'] = article.get('source')
            results.append(res)

        logging.info('Keyword query success')
        return results

    else:
        logging.error('Keyword query failed')
        return []

# query with several keywords
def findWithKeywordLists(keywords):
    logging.info('Start query with keywords list')
    if type(keywords) is list or keywords != []:
        nyt = nyt_api()
        results  = []
        for k in keywords:
            articles = nyt.article_search(
                query=k,
                results=10, #display 10 results
            )

            for article in articles:
                res = dict()
                res['WebURL'] = article.get('web_url')
                res['Snippet'] = article.get('snippet')
                res['Source'] = article.get('source')
                results.append(res)

        logging.info('Keywords list query success')
        return results

    else:
        logging.error('Keywords list query failed')
        return []

# query using day month year
def findWithDMY(year2, year1, month2, month1, day2, day1, keywords):
    logging.info('Start query with date month time')
    if type(year2) != str or type(year1) != str or type(month2) != str or type(month1) != str or type(day2) != str or type(day1) != str or type(keywords) != list or keywords is None or keywords == []:
        logging.error('Date month time query failed')
        return []
    else:
        try:
            yeari = int(year1)
            monthi = int(month1)
            dayi = int(day1)
            yeari2 = int(year2)
            monthi2 = int(month2)
            dayi2 = int(day2)
        except ValueError as e:
            logging.error('Date month time query failed')
            return []

        if 0 < monthi < 13 and 0 < monthi2 < 13 and yeari2 <= datetime.datetime.now().year and yeari <= datetime.datetime.now().year and 0 < dayi <= 31 and 0 < dayi2 <= 31 and yeari <= yeari2 and monthi <= monthi2 and dayi < dayi2:
            nyt = nyt_api()
            results = []
            for k in keywords:
                articles = nyt.article_search(
                    query=k,
                    results=10,
                    dates={
                        "begin": datetime.datetime(yeari, monthi, dayi),
                        "end": datetime.datetime(yeari2, monthi2, dayi2),
                    },
                    options={
                        "sort": "oldest", #filter from oldest data
                    }
                )
                for article in articles:
                    res = dict()
                    res['WebURL'] = article.get('web_url')
                    res['Snippet'] = article.get('snippet')
                    res['Source'] = article.get('source')
                    results.append(res)

            return results
