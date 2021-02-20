import json

def uploader(x):
    py2Json = json.dumps(x)
    return py2Json

if __name__ == '__main__':
    a = {'name':'Sarah', 'age': 24, 'isEmployed': True }

    test = uploader(a)
    print(test)
