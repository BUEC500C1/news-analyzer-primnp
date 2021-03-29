from newsingester import *

def one_query():
    input1 = ['nyc']
    res1 = ni.keyword_query(input1)
    assert type(Result) == list
    assert type(Result[0]) == dict

    validquery2 = ["hats", "bananas", "apples"]
    Result = ni.keyword_query(validquery2)
    assert type(Result) == list
    assert type(Result[0]) == dict

    #Invalid Test
    invalidquery1 = 1
    Result = ni.keyword_query(invalidquery1)
    assert Result == []
    invalidquery2 = []
    Result = ni.keyword_query(invalidquery2)
    assert Result == []
    
def lists_query():
    assert GetKeywordsSentimentData() == "(keywords, sentiment) data stat"
    assert GetFileSource() == "file source"
    assert GetSearchData() == "files with the stated keywords/sentiment"

def dmy_query():
    assert UpdateFile() == "updated file"
