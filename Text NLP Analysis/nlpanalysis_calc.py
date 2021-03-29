#based on https://googleapis.dev/python/language/latest/usage.html#documents
import logging
import sys
from google.cloud import language_v1
import os

client = language_v1.LanguageServiceClient()

logging.basicConfig(filename='nlp.log', level=logging.DEBUG, format='[%(levelname)s] %(asctime)s %(message)s')

def returnSentiment(text):
    logging.info('Sentiment analyzing initiated')
    if type(text) is str:
        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        sentiment_score = sentiment.magnitude * sentiment.score

        logging.info('Sentiment analyzed')

        return sentiment_score

    else:
        logging.error('Error when analyzing sentiment')
        return []

def returnEntities(text):
    logging.info('Entities analyzing initiated')
    if type(text) is str:
        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        response = client.analyze_entities(request={'document': document})
        results = []

        for ent in response.entities:
            results.append(ent.name)

        logging.info('Entities analyzed')
        logging.info('Entities found:')

        for res in results:
            logging.info("\t" + res)

        return results

    else:
        logging.error('Error when analyzing entities')
        return []

def returnEntitiesAndSentiments(text):
    logging.info('Entities-sentiments analyzing initiated')
    if type(text) is str:
        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        response = client.analyze_entity_sentiment(request={'document': document})
        results = []

        for ent in response.entities:
            res = dict()
            res['Entity'] = ent.name
            res['Score'] = ent.sentiment.score * ent.sentiment.magnitude
            results.append(res)

        logging.info('Entities sentiments analyzed')

        return results

    else:
        logging.error('Error when analyzing entities sentiments')
        return []


def classifyContent(text):
    logging.info('content classification analyzing initiated')
    if type(text) is str:
        textlist = text.split()
        if len(textlist) < 20: #to avoid 400 Invalid text content: too few tokens (words) to process.
            logging.info('Not enough text')
            return []

        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        response = client.classify_text(request={'document': document})
        results = []

        for cat in response.categories:
            res = dict()
            res['Category'] = cat.name
            res['Score'] = cat.confidence
            results.append(res)

        # if (results != []):
        logging.info('content classification analyzed')
        return results
        # else:
        #     logging.info('Not enough text')
        #     return []
    else:
        logging.error('Error when analyzing content classification')
        return []
