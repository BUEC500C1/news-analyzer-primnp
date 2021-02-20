from nlpanalysis import *

def test_create():
    assert searchOnKeywords() == "list of files with keywords"
    assert searchRepeatedWords() == "list of repeated words & their frequency"
    assert searchCommonKeywords() == "the most common keyword(s)"
    assert linkDocViaKeywords() == "possibly related documents"
    assert findContentSentiment() == "sentiment"
    assert linkKeywordsandSentiment() == "relationship between keywords & sentiment in numbers"
    assert linkPreviousSearch() == "search recommendations"
    assert translateText() == "translated text"
    assert findBiasOnKeywords() == "bias"

def test_read():
    assert searchBoolean() == "boolean function"
    assert GetSearchHistory() == "(keywords, sentiments)"
    assert ClassifyDatas() == "data format: xx"

def test_update():
    assert UpdateBias() == "bias updated"
    assert UpdateLanguage() == "language updated"

def test_delete():
    assert RemoveBiasData() == "Bias removed"
