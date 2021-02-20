from newsingester import *

def test_create():
    assert ingestFile() == "test create file"
    assert searchOnKeywords() == "list of files with keywords"
    assert searchOnSentiment() == "list of files with sentiment"
    assert findContentSentiment() == "sentiment"
    assert linkKeywordsandSentiment() == "relationship between keywords & sentiment in numbers"
    assert linkSearchResultandUploadedContent() == "database files that matched uploaded files"
    assert searchCommonKeywords() == "the most common keyword(s)"

def test_read():
    assert GetKeywordsSentimentData() == "(keywords, sentiment) data stat"
    assert GetFileSource() == "file source"
    assert GetSearchData() == "files with the stated keywords/sentiment"

def test_update():
    assert UpdateFile() == "updated file"

def test_delete():
    assert RemoveCommonKeywords() == "keywords deleted"
    assert RemoveContentSentiment() == "sentiment deleted"
