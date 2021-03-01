from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#create
class ingestFile(Resource):
    def get(self):
        return {'about': 'file ingested'}

    def post(self):
        json_file = request.get_json()
        return {'file ingested': json_file}, 201

def searchOnKeywords():
    #input keywords
    #search through database, using File.Text_Fields, Text, find files which has the Keywords
    #search through database, using File.Text_Fields, Keywords in case file already has common keywords logged
    #return list of files with keywords
    return "list of files with keywords"

def searchRepeatedWords():
    #input file
    #search throug file.text_fileds.text to find repeated words
    #save stats of repeated words and output them
    return "list of repeated words & their frequency"

def searchCommonKeywords():
    #input file
    #pseudo implementation
    #use searchOnKeywords, then go through the output file, find how many times the keywords present
    #log keywords appearance stat, out a keyword which has highest stat
    return "the most common keyword(s)"

def linkDocViaKeywords():
    #input keywords
    #do searchOnKeywords then findContentSentiment
    #then match the keywords from searchOnKeywords with sentiment from findContentSentiment
    #match files with has the same linkKeywordsandSentiment relationship
    return "possibly related documents"

def findContentSentiment():
    #input filecontent
    #if File.Text_Fields, Sentiment == NULL
    #search through database, with linkKeywordsandSentiment() and File.Text_Fields, Keywords to find best matched sentiment to logged keywords
    #return sentiments
    return "sentiment"

def linkKeywordsandSentiment():
    #input file
    #machine learning? record statistics of matched sentiment - Keywords
    #output user the stats of matched pair - higher stats mean related to the following keywords/sentiment
    return "relationship between keywords & sentiment in numbers"

def linkPreviousSearch():
    #run GetSearchHistory
    #based on result, run searchOnKeywords  / searchCommonKeywords to get search recommendations
    return "search recommendations"

def translateText():
    #input keywords
    #use existing translate API, match the text with possible translation
    #determine sentiment of the translation, take high linkKeywordsandSentiment as a final translation
    #call UpdateLanguage()
    return "translated text"

def findBiasOnKeywords():
    #if input is file
        #find commonkeywords using searchCommonKeywords
        #do linkDocViaKeywords on CommonKeywords
        #with result from linkDocViaKeywords, determine the common reapeated words (CRW)
        #compare result CRW with repeated words of the file itself
        #findContentSentiment on the common repeated words and save the value pair
        #bias is the sentiment from above step
    #if input is a keyword
        #do linkKeywordsandSentiment on a keyword
        #bias is the result from the above step with highest stat
    return "bias"

#read
class ReadFile(Resource):
    def get(self, file_id):
        return {'about': file_id}, 201

def searchBoolean():
    #define boolean parameters and their functions accordingly
    #return correct boolean operations functions for search
    return "boolean function"

def GetSearchHistory():
    #find previous search based on keywords/sentiments/Bias
    #record the keywords, sentiments
    return "(keywords, sentiments)"

def ClassifyDatas():
    #input phrases
    #compare the phrases with other similar phrases in existing database
    #determine similarities, output the text format with highest similarities to given phrases
    return "data format: xx"

#updated
class UpdateFile(Resource):
    def get(self, file_id):
        return {'updated': file_id}

    #just place here to indicate there should be a PUT http request, PUT won't work as of now
    def put(self):
        edit_json = request.get_json()
        return {'edited': edit_json}, 201

def UpdateBias():
    #if input is file
        #file.file_content.time_modified = timestamp when modifying event
        #update file.file_content.bias
    #if input is text
        #file.file_content.time_modified = timestamp when modifying event
        #update file.file_content.keywords.bias
    return "bias updated"

def UpdateLanguage():
    #change file.text_fields.keywords.language to correct translated language according to translateText()
    return "language updated"

#delete
# class DeleteFile(Resource):
#     def delete(self)
def RemoveBiasData():
    #if input (BiasInfo, keyword, file)
        #file.file_content.Time_modified = timestamp when deleted event
        #delete file.text_fields.keyword.bias if file.text_fields.keyword.bias == BiasInfo
    #if input (BiasInfo,'' , file)
        #file.file_content.Time_modified = timestamp when deleted event
        #delete file.text_fields.bias if file.text_fields.bias == BiasInfo
    return "Bias removed"


@app.route("/")
def index():
    return render_template("nlphome.html")

api.add_resource(ingestFile, '/file')
api.add_resource(UpdateFile, '/file/file_content/<int:file_id>')

if __name__ == '__main__':
    app.run(debug=True)
