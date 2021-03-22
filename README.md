# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom

### 02/20/2021
**Homework 2 Phase 1** are in different modules folder. Each folder consists of readme, python file, python test file.

Readme consists of:
  * if entity-base API:
    * User Stories
    * JSON requests and responses
  * if procedure-base API
    * User Stories
    * List of Functions
    * Example data
    * Possible operations

---

### 02/28/2021
**Homework 2 Phase 2**

**Works Completed**
1. Integrated *flask_restful* to each of the module to make them become a full RESTFUL system (aka create flask applications)
    * each API modules are not fully implemented; they are stub APIs serve to demonstrate possible features

example partial implementations of flask_restful:
```Python
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class FileUploader(Resource):
    def get(self):
        return {'about': 'test create file'}
        # return FILES

    def post(self):
        json_file = request.get_json()
        return {'file sent': json_file}, 201
```

2. Deploy multiple flask applications (API Modules: Secure File Uploader, News Feed Ingester, Text NLP Analysis) to AWS EC2 instance

**Public IPv4 Address: 3.140.234.103**

*Table 1 Modules and port hosted*
| Module        | Port |
| ------- | -------|
| Secure File Uploader      | 80 |
| News Feed Ingester      | 8008 |
| Text NLP Analysis |  8080 |


3. Create a simple HTML page to and render the HTML template on each modules
* To view HTML page for each module:
    * 3.140.234.103:Port of the module

Example: 
> 3.140.234.103:8080 
<img src="/Images/hw2phase2_test.png" width="65%" />

---
### 03/01/2021
**Homework 2 Phase 3 First Deliverable**

NOTE: testmongo.py has not been deployed to AWS - will work on this after

**Works Completed**
1. Setup MongoDB and integrate into flask (view in testmongo.py)
2. Create database (flask-mongoDB-atlas)


### 03/7/2021
**Homework 2 Phase 3 Second Deliverable**

**Works Completed**
1. Extract Text from PDF files -- still need to work on ensuring text is extracted correctly
2. Store Data in Database (view in testmongo.py)

<img src="/Images/phase2_deli2.png" width="65%" />

### 03/21/2021
**Continue Working on Homework 2**

1. Set up google NLP API
2. test the gooogle NLP API with text input & return sentimment
