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
1. Integrated *flask_restful* to each of the module to make them become a full RESTFUL system
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
> 3.140.234.103:8008 
<img src="/Images/hw2phase2_test.png" width="65%" />

