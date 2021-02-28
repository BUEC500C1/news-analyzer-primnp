from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#Note: testing RESTFUL functionalities, not real implementations, will put implementations for HW2 Phase 3

#create
class ingestFile(Resource):
    def get(self):
        return {'about': 'test file'}

    def post(self):
        json_file = request.get_json()
        return {'file sent': json_file}, 201
#def ingestFile():
    #input file
    #pseudo implementation
    # file.time_stamp = event(upload, timestamp)
    # if filename == NULL
    #     return "Error filename"
    # file.filename = filename
    # file.userID = 20
    # file.permissions = 20, 21
    # file.id = "/file/011"
    # file.text = "a very long text"
    # file.fileURL = "https://example.test/file/011/20"
    # ...
    #return "test create file"

def searchOnKeywords():
    #input keywords
    #pseudo implementation
    #search through database, using File.Text_Fields, Text, find files which has the Keywords
    #search through database, using File.Text_Fields, Keywords in case file already has common keywords logged
    #return list of files with keywords
    return "list of files with keywords"

def searchOnSentiment():
    #input sentiment
    #pseudo implementation
    #search through database, using File.Text_Fields, Sentiment (works on file which already has sentiment logged)
    #return list of files with the stated sentiment
    return "list of files with sentiment"

def findContentSentiment():
    #input filecontent
    #pseudo implementation
    #if File.Text_Fields, Sentiment == NULL
    #search through database, with linkKeywordsandSentiment() and File.Text_Fields, Keywords to find best matched sentiment to logged keywords
    #return sentiments
    return "sentiment"

def linkKeywordsandSentiment():
    #input file
    #pseudo implementation
    #machine learning? record statistics of matched sentiment - Keywords
    #output user the stats of matched pair - higher stats mean related to the following keywords/sentiment
    return "relationship between keywords & sentiment in numbers"

def linkSearchResultandUploadedContent():
    #input commonkeywords
    #pseudo implementation
    #match file in database and uploaded file with common keywords
    return "database files that matched uploaded files"

def searchCommonKeywords():
    #input file
    #pseudo implementation
    #use searchOnKeywords, then go thru the output file, find how many times the keywords present
    #log keywords appearance stat, out a keyword which has highest stat
    return "the most common keyword(s)"

#Read
def GetKeywordsSentimentData():
    #input (keyword,sentiment)
    #return stats of value pair keywords, sentiment
    return "(keywords, sentiment) data stat"

def GetFileSource():
    #input file
    #file.Metadata.FileSource
    return "file source"

def GetSearchData():
    #input keywords or sentiment
    #searchOnKeywords
    #searchOnSentiment
    return "files with the stated keywords/sentiment"

#Update
class UpdateFile(Resource):
    def get(self, file_id):
        return {'updated': file_id}

    #just place here to indicate there should be a PUT http request, PUT won't work as of now
    def put(self):
        json_file = request.get_json()
        return {'updated': json_file}, 201
#def UpdateFile():
    #input file
    #file.file_content.time_modified = timestamp when modifying event
    #possible modify data scenarios
    #file.file_content.file_name - to change file name
    #file.file_content.permissions - to change who has access to the files
    #file.file_content.file_tags - to change file tags
    #file.file_content.notes - to change file notes
    #return "updated file"

#Delete
def RemoveCommonKeywords():
    #input (keywords, file)
    #file.file_content.Time_modified = timestamp when delete event
    #delete file.text_fields.keywords if file.text_fields.keywords == keywords
    return "keywords deleted"

def RemoveContentSentiment():
    #input (sentiment, file)
    ##file.file_content.Time_modified = timestamp when delete event
    #delete file.text_fields.sentiment if file.text_fields.sentiment == sentiment
    return "sentiment deleted"


@app.route("/")
def index():
    return 'News Feed Ingester API with RESTFUL'

api.add_resource(ingestFile, '/file')
api.add_resource(UpdateFile, '/file/file_content/<int:file_id>')


if __name__ == '__main__':
    app.run(debug=True)
