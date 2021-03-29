from flask import Flask, request, render_template, jsonify, request, redirect, url_for
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
import os
from werkzeug.utils import secure_filename
import PyPDF2
import json
import logging
import requests
#import db
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb+srv://dbUser:1PASSword1@flask-mongodb-atlas.e8vt3.mongodb.net/file-collection-ingester?retryWrites=true&w=majority"
mongo = PyMongo(app)
UPLOAD_FOLDER = './files'

logging.basicConfig(filename='app.log', level=logging.INFO)

db_operations = mongo.db.users
db_file = mongo.db.files_collection
db_extracted = mongo.db.extracted_data

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#CRUD Operations
#Create
# @app.route('/create')
# def create():
#     new_user = {'Name' : 'user1', 'First_name' : 'test1', 'Last_name': 'user1', 'Display_name': 'test1 user1', 'Email': 'test1@example.test', 'Active': True }
#     db_operations.insert_one(new_user)
#     #print(user['Name'],'Created successfully')
#     result = {'result' : 'Created successfully'}
#     return result
#
# @app.route('/create-many')
# def create_many():
#     new_user_1 = {'Name' : 'user2', 'First_name' : 'test2', 'Last_name': 'user2', 'Display_name': 'test2 user2', 'Email': 'test2@example.test', 'Active': True }
#     new_user_2 = {'Name' : 'user3', 'First_name' : 'test3', 'Last_name': 'user3', 'Display_name': 'test3 user3', 'Email': 'test3@example.test', 'Active': False }
#     new_user_3 = {'Name' : 'user4', 'First_name' : 'test4', 'Last_name': 'user4', 'Display_name': 'test4 user4', 'Email': 'test4@example.test', 'Active': True }
#     new_users = [new_user_1, new_user_2, new_user_3]
#     db_operations.insert_many(new_users)
#     result = {'result' : 'Created successfully'}
#     return result
#
# #Read
#
# @app.route('/read')
# def read():
#     users = db_operations.find()
#     output = [{'Name' : user['Name'], 'First_name' : user['First_name'], 'Last_name': user['Last_name'], 'Display_name': user['Display_name'], 'Email': user['Email'], 'Active': user['Active']} for user in users]
#     #print(output)
#     return jsonify(output)
#
# @app.route('/read-with-filter')
# def read_with_filter():
#     filt = {'Name' : 'user1'}
#     users = db_operations.find(filt)
#     output = [{'Name' : user['Name'], 'First_name' : user['First_name'], 'Last_name': user['Last_name'], 'Display_name': user['Display_name'], 'Email': user['Email'], 'Active': user['Active']}  for user in users]
#     #print(output)
#     return jsonify(output)
#
# @app.route('/read-one')
# def read_one():
#     filt = {'Name' : 'user1'}
#     user = db_operations.find_one(filt)
#     output = {'Name' : user['Name'], 'First_name' : user['First_name'], 'Last_name': user['Last_name'], 'Display_name': user['Display_name'], 'Email': user['Email'], 'Active': user['Active']}
#     #print(output)
#     return jsonify(output)
#
# #Update
#
# @app.route('/update')
# def update():
#     updated_user = {"$set": {'Active' : False}}
#     filt = {'Name' : 'user1'}
#     db_operations.update_one(filt, updated_user)
#     result = {'result' : 'Updated successfully'}
#     return result
#
# @app.route('/update-many')
# def update_many():
#     updated_user = {"$set": {'Active' : False}}
#     filt = {'Name' : 'user1'}
#     db_operations.update_many(filt, updated_user)
#     result = {'result' : 'Updated successfully'}
#     return result
#
# @app.route('/update-if-exist-or-insert')
# def update_if_exist_or_insert():
#     updated_user = {"$set": {'Active' : False}}
#     filt = {'Name' : 'user1'}
#     db_operations.update_one(filt, updated_user, upsert=True)
#     result = {'result' : 'Done successfully'}
#     return result
#
# #Delete
#
# @app.route('/delete')
# def delete():
#     filt = {'Name' : 'user3'}
#     db_operations.delete_one(filt)
#     result = {'result' : 'Deleted successfully'}
#     return result
#
# @app.route('/delete-many')
# def delete_many():
#     filt = {'Name' : 'user3'}
#     db_operations.delete_many(filt)
#     result = {'result' : 'Deleted successfully'}
#     return result

#Saving /  retrieving / extracting files
# <input type="file" name="new_file"><br><br>
@app.route('/')
def index():
    return '''
        <h1>File Uploader Ingester</h1>
        <form method="POST" action="/save-file" enctype="multipart/form-data">
            <h2>File Uploader</h1>
            <label for="name">File name</label>
            <input type="text" name="name" id="name">
            <input type="file" name="new_file"><br><br>
            <input type="submit" value="submit">
        </form>
        <form method="POST" action="/extract-file" enctype="multipart/form-data">
            <h2>Extract PDF</h2>
            <label for="name">File name</label>
            <input type="text" name="name" id="name">
            <input type="file" name="new_file"><br><br>
            <input type="submit" value="submit">
        </form>
    '''

@app.route('/save-file', methods=['POST'])
def save_file():
    if 'new_file' in request.files:
        new_file = request.files['new_file']
        mongo.save_file(new_file.filename, new_file)
        data = {'Name' : request.values.get('name'), 'File Name' : new_file.filename}
        db_file.insert_one(data)
        nameurl = request.values.get('name')
        logging.info('Uploaded Successfully')
    return redirect(url_for('retrieve_file', name=nameurl))
    # redirect('/')

@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/retrieve-file/<name>')
def retrieve_file(name):
    filt = {'Name' : name}
    f = db_file.find_one(filt)
    #file_name = f['File Name']
    return f'''
    <h2>Uploaded "{name}: {f['File Name']}" Successfully</h2>
    <embed src="{url_for('file', filename=f['File Name'])}">
    '''
    # mongo.send_file(file_name)

# @app.route('/extract-pdf/<pdfname>', methods=['GET'])
# def extract_pdf(pdfname):
#     filt = {'Name' : 'user1'}
#     user = db_operations.find_one(filt)
#     output = {'Name' : user['Name'], 'First_name' : user['First_name'], 'Last_name': user['Last_name'], 'Display_name': user['Display_name'], 'Email': user['Email'], 'Active': user['Active']}
#     #print(output)
#     return jsonify(output)
# @app.route('/uploader', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#     return 'file uploaded successfully'

#
@app.route('/extract-file', methods=['POST'])
def extract_file():
    if 'new_file' in request.files:
        new_file = request.files['new_file']
        # mongo.save_file(new_file.filename, new_file)

        # create the instance folders when setting up your app
        os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)

        # when saving the file
        new_file.save(os.path.join(app.instance_path, 'htmlfi', secure_filename(new_file.filename)))

        if allowed_file(new_file.filename):
            # file = requests.get('http://127.0.0.1:5000/'+url_for('file', filename=f['File Name']))
            # with open('test_file.pdf', 'wb') as f:
            #     f.write(file.raw)
            file_path = os.path.join(app.instance_path, 'htmlfi', secure_filename(new_file.filename))

            file_obj = open(file_path, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(file_obj)
            pdata = ""
            tdata = ""
            for i in range(pdf_reader.numPages):
                page = pdf_reader.getPage(i)
                pdata = page.extractText()
                tdata += pdata

            file_obj.close()
            data = {'Name': request.values.get('name'), 'TextExtracted': tdata, 'OriginalPDF': new_file.filename}

            nameurl = request.values.get('name')
            db_extracted.insert_one(data)
        else:
            print("only .pdf is supported")
    else:
        print("failed extracting file")

    return redirect(url_for('retrieve_info', name=nameurl))
    # return f'''
    # <embed src="{url_for('file', filename=f['File Name'])}">
    # '''
# @app.route('/retrieve-text/<name>')
# def retrieve_text(name):
#     filt = {'Name' : name}
#     fin = db_extracted.find(filt)
#     #ouput = fin['TextExtracted']
#     output = [{final['TextExtracted']} for final in fin]
#
#     return f'''
#     <h2>Extracted "{fin['OriginalPDF']}" successfully and saved into file name: "{name}"</h2>
#     # <p>Extracted Text:{output}</p>
#     '''

@app.route('/retrieve-info/<name>')
def retrieve_info(name):
    filt = {'Name' : name}
    text_col = db_extracted.find(filt)
    output = [{'Name' : text['Name'], 'TextExtracted' : text['TextExtracted'], 'OriginalPDF': text['OriginalPDF']} for text in text_col]
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
