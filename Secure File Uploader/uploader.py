from flask import Flask, request, render_template, jsonify, request, redirect, url_for
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
import os
from werkzeug.utils import secure_filename
import PyPDF2
from datetime import datetime
import json
import logging
#import db
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb+srv://dbUser:1PASSword1@flask-mongodb-atlas.e8vt3.mongodb.net/file-collection-ingester?retryWrites=true&w=majority"
mongo = PyMongo(app)

logging.basicConfig(filename='uploader.log', level=logging.INFO, format='[%(levelname)s] %(asctime)s %(message)s')

db_file = mongo.db.files_collection
db_extracted = mongo.db.extracted_data

# check for allowed file when extracting data, only pdf allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('uploader_home'))

@app.route('/uploader')
def uploader_home():
    return '''
        <h1>File Uploader Ingester</h1>
        <form method="POST" action="/uploader/save-file" enctype="multipart/form-data">
            <h2>File Uploader</h2>
            <label for="name">File name</label>
            <input type="text" name="name" id="name">
            <input type="file" name="new_file"><br><br>
            <input type="submit" value="upload">
        </form>
        <form method="POST" action="/uploader/extract-file" enctype="multipart/form-data">
            <h2>Extract PDF</h2>
            <label for="name">File name</label>
            <input type="text" name="name" id="name">
            <input type="file" name="new_file"><br><br>
            <input type="submit" value="extract">
        </form>
    '''

# Create
@app.route('/uploader/save-file', methods=['POST'])
def save_file():
    logging.info('Upload initiated')
    if 'new_file' in request.files:
        new_file = request.files['new_file']
        mongo.save_file(new_file.filename, new_file)
        data = {'Name' : request.values.get('name'), 'File Name' : new_file.filename, 'Date Time Uploaded': str(datetime.now()), 'Date Time Updated': "not available"}
        db_file.insert_one(data)
        nameurl = request.values.get('name')
        logging.info('Uploaded Successfully')
    else:
        logging.error('Upload failed')
        return "Upload failed"
    return redirect(url_for('retrieve_filejson', name=nameurl))
    # redirect('/')

# Read and show file to user
@app.route('/uploader/file/<filename>')
def file(filename):
    return mongo.send_file(filename)

@app.route('/uploader/view-file/<name>')
def view_file(name):
    filt = {'Name' : name}
    f = db_file.find_one(filt)
    #file_name = f['File Name']
    return f'''
    <h2>Viewing -- Name:"{name}" from File Name:"{f['File Name']}"</h2>
    <embed src="{url_for('file', filename=f['File Name'])}">
    '''

# read all uploaded files
@app.route('/uploader/retrieve-filejson/view-all')
def view_allfiles():
    files = db_file.find({})
    output = [{'Name' : fs['Name'], 'File Name' : fs['File Name'], 'Date Time Uploaded': fs['Date Time Uploaded'], 'Date Time Updated': fs['Date Time Updated']} for fs in files]
    return jsonify(output)

# Read and output file info as json
@app.route('/uploader/retrieve-filejson/<name>')
def retrieve_filejson(name):
    filt = {'Name' : name}
    fs = db_file.find_one(filt)
    # if (!fs):
    #     return "No file available"
    # else:
    output = {'Name' : fs['Name'], 'File Name' : fs['File Name'], 'Date Time Uploaded': fs['Date Time Uploaded'], 'Date Time Updated': fs['Date Time Updated']}
    if (output == {}):
        return "Files Not Available"
    else:
        return jsonify(output)

# Update file name + also update with the time that new name is updated
@app.route('/uploader/retrieve-filejson/<oldname>/update/<newname>')
def update_uploadedfile(oldname, newname):
    updated_info = {"$set": {'Name' : newname, 'Date Time Updated': str(datetime.now())}}
    filt = {'Name' : oldname}
    db_file.update_one(filt, updated_info, upsert=True)
    logging.info('Updated file successfully')
    # result = {'result' : 'Done successfully'}
    return redirect(url_for('retrieve_filejson', name=newname))

# Delete all files with the same name
@app.route('/uploader/retrieve-filejson/delete-many/<name>')
def delete_many(name):
    filt = {'Name' : name}
    db_file.delete_many(filt)
    result = {'result' : 'Deleted successfully'}
    return result

# Delete all files from the collection
@app.route('/uploader/retrieve-filejson/delete-all')
def delete_all():
    db_file.remove()
    result = {'result' : 'Deleted successfully'}
    return result

# ================================================================ #
# Extract file from new upload
@app.route('/uploader/extract-file', methods=['POST'])
def extract_file():
    logging.info('Extract file initiated')
    if 'new_file' in request.files:
        new_file = request.files['new_file']

        # create the instance folders when setting up your app
        os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)

        # when saving the file
        new_file.save(os.path.join(app.instance_path, 'htmlfi', secure_filename(new_file.filename)))

        if allowed_file(new_file.filename):
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
            data = {'Name': request.values.get('name'), 'File Name' : new_file.filename, 'Date Time Uploaded': str(datetime.now()),'Date Time Updated': "not available", 'TextExtracted': tdata}
            logging.info('Extracted Successfully')
            nameurl = request.values.get('name')
            db_extracted.insert_one(data)
        else:
            logging.error('Only .pdf is supported')
            return('Only .pdf is supported')
    else:
        logging.error('Extract file failed')
        return('Extract file failed')

    return redirect(url_for('retrieve_text', name=nameurl))

# read extracted text
@app.route('/uploader/retrieve-text/<name>')
def retrieve_text(name):
    filt = {'Name' : name}
    text_col = db_extracted.find(filt)
    output = [{'Name' : text['Name'], 'File Name': text['File Name'], 'Date Time Uploaded': text['Date Time Uploaded'], 'Date Time Updated': text['Date Time Updated'], 'TextExtracted' : text['TextExtracted']} for text in text_col]
    return jsonify(output)

# read all extracted files
@app.route('/uploader/retrieve-text/view-all')
def view_alltext():
    files = db_extracted.find({})
    output = [{'Name' : fs['Name'], 'File Name' : fs['File Name'], 'Date Time Uploaded': fs['Date Time Uploaded'], 'Date Time Updated': fs['Date Time Updated'], 'TextExtracted' : fs['TextExtracted']} for fs in files]
    return jsonify(output)

# Update file name + also update with the time that new name is updated
@app.route('/uploader/retrieve-text/<oldname>/update/<newname>')
def update_extractfile(oldname, newname):
    updated_info = {"$set": {'Name' : newname, 'Date Time Updated': str(datetime.now())}}
    filt = {'Name' : oldname}
    db_extracted.update_one(filt, updated_info, upsert=True)
    logging.info('Updated extracted file successfully')
    return redirect(url_for('retrieve_text', name=newname))

# Delete all files with the same name
@app.route('/uploader/retrieve-text/delete-many/<name>')
def delete_extractedmany(name):
    filt = {'Name' : name}
    db_extracted.delete_many(filt)
    result = {'result' : 'Deleted successfully'}
    return result

# delete all files in the collection
@app.route('/uploader/retrieve-text/delete-all')
def delete_alltext():
    db_extracted.remove()
    result = {'result' : 'Deleted successfully'}
    return result

if __name__ == '__main__':
    app.run(debug=True)
