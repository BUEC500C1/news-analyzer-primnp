from flask import Flask, request, render_template, jsonify, request, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
import PyPDF2
import json
#import db
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb+srv://dbUser:1PASSword1@flask-mongodb-atlas.e8vt3.mongodb.net/file-collection-ingester?retryWrites=true&w=majority"
mongo = PyMongo(app)

db_operations = mongo.db.users
db_file = mongo.db.files_collection
db_extracted = mongo.db.extracted_data

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#CRUD Operations
#Create
@app.route('/create')
def create():
    new_user = {'Name' : 'user1', 'First_name' : 'test1', 'Last_name': 'user1', 'Display_name': 'test1 user1', 'Email': 'test1@example.test', 'Active': True }
    db_operations.insert_one(new_user)
    #print(user['Name'],'Created successfully')
    result = {'result' : 'Created successfully'}
    return result

@app.route('/create-many')
def create_many():
    new_user_1 = {'Name' : 'user2', 'First_name' : 'test2', 'Last_name': 'user2', 'Display_name': 'test2 user2', 'Email': 'test2@example.test', 'Active': True }
    new_user_2 = {'Name' : 'user3', 'First_name' : 'test3', 'Last_name': 'user3', 'Display_name': 'test3 user3', 'Email': 'test3@example.test', 'Active': False }
    new_user_3 = {'Name' : 'user4', 'First_name' : 'test4', 'Last_name': 'user4', 'Display_name': 'test4 user4', 'Email': 'test4@example.test', 'Active': True }
    new_users = [new_user_1, new_user_2, new_user_3]
    db_operations.insert_many(new_users)
    result = {'result' : 'Created successfully'}
    return result

#Read

@app.route('/read')
def read():
    users = db_operations.find()
    output = [{'Name' : user['Name'], 'First_name' : user['First_name'], 'Last_name': user['Last_name'], 'Display_name': user['Display_name'], 'Email': user['Email'], 'Active': user['Active']} for user in users]
    #print(output)
    return jsonify(output)

@app.route('/read-with-filter')
def read_with_filter():
    filt = {'Name' : 'user1'}
    users = db_operations.find(filt)
    output = [{'Name' : user['Name'], 'First_name' : user['First_name'], 'Last_name': user['Last_name'], 'Display_name': user['Display_name'], 'Email': user['Email'], 'Active': user['Active']}  for user in users]
    #print(output)
    return jsonify(output)

@app.route('/read-one')
def read_one():
    filt = {'Name' : 'user1'}
    user = db_operations.find_one(filt)
    output = {'Name' : user['Name'], 'First_name' : user['First_name'], 'Last_name': user['Last_name'], 'Display_name': user['Display_name'], 'Email': user['Email'], 'Active': user['Active']}
    #print(output)
    return jsonify(output)

#Update

@app.route('/update')
def update():
    updated_user = {"$set": {'Active' : False}}
    filt = {'Name' : 'user1'}
    db_operations.update_one(filt, updated_user)
    result = {'result' : 'Updated successfully'}
    return result

@app.route('/update-many')
def update_many():
    updated_user = {"$set": {'Active' : False}}
    filt = {'Name' : 'user1'}
    db_operations.update_many(filt, updated_user)
    result = {'result' : 'Updated successfully'}
    return result

@app.route('/update-if-exist-or-insert')
def update_if_exist_or_insert():
    updated_user = {"$set": {'Active' : False}}
    filt = {'Name' : 'user1'}
    db_operations.update_one(filt, updated_user, upsert=True)
    result = {'result' : 'Done successfully'}
    return result

#Delete

@app.route('/delete')
def delete():
    filt = {'Name' : 'user3'}
    db_operations.delete_one(filt)
    result = {'result' : 'Deleted successfully'}
    return result

@app.route('/delete-many')
def delete_many():
    filt = {'Name' : 'user3'}
    db_operations.delete_many(filt)
    result = {'result' : 'Deleted successfully'}
    return result

#Saving /  retrieving / extracting files

@app.route('/')
def index():
    return '''
        <h1>File Uploader Ingester</h1>
        <form method="POST" action="/save-file" enctype="multipart/form-data">
            <h2>File Uploader</h1>
            <label for="name">File name</label>
            <input type="text" name="name" id="name">
            <input type="file" name="new_file"><br><br>
            <input type="submit">
        </form>
        <form method="POST" action="/extract-file" ecntype="multipart/form-data">
            <h2>Extract PDF</h2>
            <label for="name">File name</label>
            <input type="text" name="name" id="name">
            <input type="file" name="new_file"><br><br>
            <input type="submit" value="extract"><br><br>
        </form>
    '''

@app.route('/save-file', methods=['POST'])
def save_file():
    if 'new_file' in request.files:
        new_file = request.files['new_file']
        mongo.save_file(new_file.filename, new_file)
        data = {'Name' : request.values.get('name'), 'File Name' : new_file.filename}
        db_file.insert_one(data)
    return redirect('/')

@app.route('/retrieve-file/<name>')
def retrieve_file(name):
    filt = {'Name' : name}
    f = db_file.find_one(filt)
    file_name = f['File Name']
    return mongo.send_file(file_name)
#
@app.route('/extract-file', methods=['POST', 'GET'])
def extract_file():
    if 'new_file' not in request.files:

        return redirect('/')

    new_file = request.files['new_file']
    mongo.save_file(new_file.filename, new_file)

    if new_file and allowed_file(new_file.filename):
        file_obj = open(new_file.filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(file_obj)
        pdata = ""
        tdata = ""
        for i in range(pdf_reader.numPages):
            page = pdf_reader.getPage(i)
            pdata = page.extractText()

            tdata += pdata
        file_obj.close()
        data = {'Name': request.values.get('name'), 'TextExtracted': tdata}
        db_extracted.insert_one(data)
    return redirect('/')

@app.route('/retrieve-text/<name>', methods=['POST', 'GET'])
def retrieve_text(name):
    filt = {'Name' : name}
    text_col = db_extracted.find(filt)
    output = [{'Name' : text['Name'], 'TextExtracted' : text['TextExtracted']} for text in text_col]
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
