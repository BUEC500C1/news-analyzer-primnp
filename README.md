# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom

## Overview
I created 3 REST API modules. Each implementation are in the respective folder:

1. Implementation of file uploader - [Secure File Uploader](https://github.com/BUEC500C1/news-analyzer-primnp/tree/main/Secure_File_Uploader)
2. Implementation of news ingester - [News Feed Ingester](https://github.com/BUEC500C1/news-analyzer-primnp/tree/main/News_Feed_Ingester)
3. Implementation of NLP - [Text NLP Analysis](https://github.com/BUEC500C1/news-analyzer-primnp/tree/main/Text_NLP_Analysis)

Please refer to video below to view demonstration of the homework. Click to view video.

[![IMAGE ALT TEXT](http://img.youtube.com/vi/XtwgpkT5K3A/0.jpg)](http://www.youtube.com/watch?v=XtwgpkT5K3A "EC500 HW2")


Please refer to video below to view all API functionalities. Click to view video.

[![IMAGE ALT TEXT](http://img.youtube.com/vi/eQoXtWo6sDg/0.jpg)](http://www.youtube.com/watch?v=eQoXtWo6sDg "EC500 HW2 All API Functionalities")




**NOTE: My Amazon EC2 instance has been running for a while. Please let me know if the ip address of REST API is not accessible.**

**Public IPv4 Address: 3.140.234.103**

*Table 1 Modules and port hosted*
| Module        | Port |
| ------- | -------|
| Secure File Uploader      | 80 |
| News Feed Ingester      | 8008 |
| Text NLP Analysis |  8080 |

* To view first EC2 instance for each module:
    * 3.140.234.103:80/ --> FOR SECURE FILE UPLOADER
    * 3.140.234.103:8008/newsfeedig --> FOR NEWS FEED INGESTER
    * 3.140.234.103:8080/nlp --> FOR TEXT NLP ANALYSIS

* Multiprocessing has not been implemented due to time constraints.

## Past Timeline
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

---
### 03/7/2021
**Homework 2 Phase 3 Second Deliverable**

**Works Completed**
1. Extract Text from PDF files -- still need to work on ensuring text is extracted correctly
2. Store Data in Database (view in testmongo.py)

<img src="/Images/phase2_deli2.png" width="65%" />

---
### 03/21/2021
**Continue Working on Homework 2**

**Works Completed**
1. Set up google NLP API & credentials
2. test the gooogle NLP API with text input & return sentiment (code runs on local machine) 
> nlpanalysis.py 

**To be completed**
1. Set up github secrets
2. Complete Sentiment the news feed search part

---
### 03/28/2021
**Wrap up Homework 2**

**completed on 03/29/2021**
1. Update readme.md for better documentation
2. Create a video, walk through how different API modules function

---
### 03/29/2021

* Working on fixing the github workflows

