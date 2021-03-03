from flask import Flask, request, render_template
from flask_restful import Resource, Api
import json
import db

app = Flask(__name__)
api = Api(app)

#Note: testing RESTFUL functionalities, not real implementations, will put implementations for HW2 Phase 3


class FileUploader(Resource):
    def get(self):
        return {'about': 'test create file'}
        # return FILES

    def post(self):
        json_file = request.get_json()
        return {'file sent': json_file}, 201

    #def delete

class EditFile(Resource):
    def get(self, file_id):
        return {'about': file_id}

    #just place here to indicate there should be a PUT http request, PUT won't work as of now
    def put(self): #def put(self, file_id):
        edit_json = request.get_json()
        return {'edited': edit_json}, 201

class User(Resource):
    def get(self):
        return {'about': 'test user'}

    def post(self):
        json_user = request.get_json()
        return {'user info sent': json_user}, 201

    #def PUT
    #def delete


# def uploader():
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
# return "test create file"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/test")
def test():
    db.db.collection.insert_one({"test":"file"})
    return "database tested"

api.add_resource(FileUploader, '/file')
api.add_resource(EditFile, '/file/File_Info/<int:file_id>')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
