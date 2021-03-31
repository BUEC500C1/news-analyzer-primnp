from uploader import *

def test_uploader():
  result = {'result' : 'Deleted successfully'}
  
  assert allowed_file('test.pdf') == True
  assert allowed_file('test.jpg') == False
  assert type(retrieve_filejson('test')) == NoneType
  assert delete_many('files') == result
  assert delete_all() == result
  assert delete_extractedmany('random') == result
  assert delete_alltext() == result
  assert type(viewalltext()) == NoneType
  
  
  
