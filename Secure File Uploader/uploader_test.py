from uploader import *

def test_uploader():
  assert uploader({"name":"Sarah", "age": 24, "isEmployed": true }) == {"name": "Sarah", "age": 24, "isEmployed": true}
