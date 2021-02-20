from uploader import *

def test_uploader():
  assert uploader({'name':'Sarah', 'age': 24, 'isEmployed': True }) == {'name':'Sarah', 'age': 24, 'isEmployed': True }
