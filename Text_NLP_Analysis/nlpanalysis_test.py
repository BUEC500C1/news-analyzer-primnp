import nlpanalysis_calc as nlp

def test_sentiment():
    input1 = "a quick brown fox"
    res = nlp.returnSentiment(input1)
    assert type(res) == float
    
    input2 = "John is very angry at that blue cat"
    res2 = nlp.returnSentiment(input2)
    assert type(res2) == float
    
    input3 = []
    res3 = nlp.returnSentiment(input3)
    assert res3 == []
  
def test_entity():
    input1 = "Bitcoin is unpredictable"
    res = nlp.returnEntities(input)
    assert type(res) == list
    
    input2 = "river flows in you"
    res2 = nlp.returnEntities(input2)
    assert type(res2) == list
    assert type(res2[0]) == str
    
    input3 = None
    res3 = nlp.returnEntities(input3)
    assert res3 == []

def test_entsent():
    input1 = "a quick brown fox jumps over a lazy dog"
    res = nlp.returnEntitiesAndSentiments(input1)
    assert type(res) == list
    assert type(res[0]) == dict
    
    input2 = ['1','2','3']
    res2 = nlp.returnEntitiesAndSentiments(input2)
    assert res2 == []

def test_conclass():
    input1 = "A quick brown fox jumps over a lazy dog. The lazy dog then disappear mysteriously. People start to wonder if a quick brown fox is a witch."
    res = nlp.classifyContent(input1)
    assert type(res) == list
    assert type(res[0]) == dict
    
    input2 = "A quick brown fox jumps over a lazy dog."
    res2 = nlp.classifyContent(input2)
    assert res2 == NULL
    
