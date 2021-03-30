from .News_Feed_Ingester import newsingester_calc as news

def test_onequery():
    input1 = ['nyc']
    res1 = news.findWithKeyword(input1)
    assert type(res1[0]) == dict

    input2 = ['apple']
    res2 = news.findWithKeyword(input2)
    assert type(res2[0]) == dict
    
    input3 = 0
    res3 = news.findWithKeyword(input3)
    assert res3 == []

def test_listsquery():
    input1 = ['nyc', 'apple', 'times']
    res1 = news.findWithKeywordLists(input1)
    assert type(res1) == dict

    input2 = 0
    res2 = news.findWithKeywordLists(input2)
    assert res2 == []
    
    input3 = []
    res3 = news.findWithKeywordLists(input3)
    assert res3 == []

def test_dmyquery():
    test1 = news.dmy_query('2021', '2021', '03', '03', '25', '15', ['grape', 'apple'])
    assert type(test1) == list
    assert type(test1[0]) == dict
    
    test2 = news.dmy_query('2021', '2021', '03', '03', '15', '25', ['grape', 'apple'])
    assert test2 == []
