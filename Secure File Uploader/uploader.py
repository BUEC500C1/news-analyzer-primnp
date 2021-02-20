import json

def uploader(x):
    py2Json = json.dumps(x)
    return py2Json

# #test
# if __name__ == '__main__':
#     #a = {'name':'Sarah', 'age': 24, 'isEmployed': True }
#     a = {
#       "err": {
#         "code": 101,
#         "message": "You don't have permission for this"
#       },
#       "status": "fail"
#     }
#     test = uploader(a)
#     print(test)
