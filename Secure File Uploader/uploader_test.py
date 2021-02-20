from uploader import *

def test_uploader():
  assert uploader({"name":"My_username", "ID": 24, "isActive": True }) == {"name": "My_username", "ID": 24, "isActive": True}
