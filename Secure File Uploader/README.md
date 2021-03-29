# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom

## User Stories - Secure File Uploader/Ingester
*  As a user, I want to upload local file to database
*  As a user, I want to upload various file types with different formatting
*  As a user, I want to see the progress of the upload whether there are any issues or the task has been completed (logging info)
*  As a user, I want to convert from PDF to text
*  As a user, I want to view/edit/delete files I have uploaded

>  Entity-based module

## Build Instructions
Aside from cloning the repository, there are several steps needed to be done to run the code properly.
First, create mongoDB atlas account. Create a data cluster on mongoDB atlas. Follow the steps to connect data cluster to application. Replacing connection_URL with your own connection URL.
```
app.config["MONGO_URI"] = your_connection_URL
```
Now your mongoDB atlas cluster is connected to flask application.

## API Requests and Responses
In this file uploader API implementation, I included mongoDB database. So the files uploaded/ingested will be stored inside my mongoDB database collection.

I created two separate database collection, one for uploading, and another for ingesting. In this entity-base API module, I have implemented CRUD.

**1. File Uploader | Data Collection: files_collection**

 1.1 *Save uploaded file to database (C) and display the saved file (R)*
  * Using POST method connected to form. When user hit submit button, POST is called to save file to mongoDB database. Data is saved to collection: files_collection.
  * Upon successful POST, user will be redirected to GET and the parameters returned will be json containing 4 parameters as stated in example below.

  URI  | HTTP Method
  ------------- | -------------
  /uploader/save-file  | POST
  /uploader/retrieve-filejson/(name) | GET

  **Successful upload response example**
  ```JSON
  {
    "Date Time Updated": "not available",
    "Date Time Uploaded": "2021-03-29 07:47:31.120301",
    "File Name": "phase2_deli2.png",
    "Name": "5"
  }
  ```
---
 1.2 *Read operations to read file inside files_collection collection in several ways (R)*
  1.2.1 View all files in files_collection database
  URI  | HTTP Method
  ------------- | -------------
  /uploader/retrieve-filejson/view-all | GET

  **Successful response example**
  ```json
  [
    {
      "Date Time Updated": "2021-03-29 02:00:34.564575",
      "Date Time Uploaded": "2021-03-29 01:58:18.471071",
      "File Name": "Screen Shot 2021-03-25 at 7.42.28 PM.png",
      "Name": "test_img"
    },
    {
      "Date Time Updated": "not available",
      "Date Time Uploaded": "2021-03-29 02:58:29.824606",
      "File Name": "test_text.pdf",
      "Name": "1"
    },
    {
      "Date Time Updated": "not available",
      "Date Time Uploaded": "2021-03-29 02:58:51.402507",
      "File Name": "PDFtest.pdf",
      "Name": "2"
    }
  ]
  ```
  1.2.2 Read one file data and also display the file (GET) -- for UI purpose
  URI  | HTTP Method
  ------------- | -------------
  /uploader/view-file/(name) | GET

  **Successful response example**
  <img src="/Images/read2.png" width="65%" />

---
1.3 *Update the name of the file stored on mongoDB files_collection (U)*
  * Update file name and also update with the time when a file is updated
  * Upon successful operation, redirect back to retrieve_filejson. Return json containing 4 parameters with new 'date time updated'

  URI  | HTTP Method
  ------------- | -------------
  /uploader/retrieve-filejson/(oldname)/update/(newname) | GET
  /uploader/retrieve-filejson/(name) | GET

  **Successful response example**
  ```json
  {
    "Date Time Updated": "2021-03-29 07:59:47.600599",
    "Date Time Uploaded": "2021-03-29 02:59:04.154874",
    "File Name": "Screen Shot 2021-03-25 at 7.07.31 PM.png",
    "Name": "5"
  }
  ```
---
1.4 *Delete file(s) stored on mongoDB files_collection (D)*
  * User can delete one file by specifying the name of the file in URI
  * User can also delete all the files stored in mongoDB files_collection collection
  * Upon successful operation, user will be shown with 'deleted successfully'

  URI  | HTTP Method
  ------------- | -------------
  /uploader/retrieve-filejson/delete-many/(name) | GET
  /uploader/retrieve-filejson/delete-all | GET

  **Successful response example**
  ```json
  {
    "result": "Deleted successfully"
  }
  ```
---
**2. File Ingester (Extract PDF) | Data Collection: extracted_data**
2.1 *Save uploaded file to database (C) and display the saved file data along with extracted text (R)*
  * Using POST method connected to form. When user hit submit button, POST is called to extract text from PDF and save data to database. Data is saved to collection: extracted_data.
  * Upon successful POST, user will be redirected to GET and the parameters returned will be json containing 5 parameters as stated in example below.

  URI  | HTTP Method
  ------------- | -------------
  /uploader/extract-file  | POST
  /uploader/retrieve-text/(name) | GET

  **Successful response example**
  ```json
  [
    {
      "Date Time Updated": "not available",
      "Date Time Uploaded": "2021-03-29 08:13:46.738869",
      "File Name": "PDFtest.pdf",
      "Name": "4e",
      "TextExtracted": "  PDF Test File  Congratulations, your computer is equipped with a PDF (Portable Document Format) reader!  You should be able to view any of the PDF documents and forms available on our site.  PDF forms are indicated by these icons: \n  or  \n.    Yukon Department of Education Box 2703 Whitehorse,Yukon Canada Y1A 2C6  Please visit our website at:  \nhttp://www.education.gov.yk.ca/\n   "
    }
  ]
  ```
---
2.2 *Read operations to read file inside extracted_data collection (R)*
  * View all files in extracted_data database collection

  URI  | HTTP Method
  ------------- | -------------
  /uploader/retrieve-text/view-all | GET

  **Successful response example**
  ```json
  [
    {
      "Date Time Updated": "not available",
      "Date Time Uploaded": "2021-03-29 03:10:56.823911",
      "File Name": "test_text.pdf",
      "Name": "1e",
      "TextExtracted": "Adobe Acrobat PDF Files\nAdobe\u00ae Portable Document Format (PDF) is a universal file format that preserves all\nof the fonts, formatting, colours and graphics of any source document, regardless of\n\nthe application and platform used to create it.\nAdobe PDF is an ideal format for electronic document distribution as it overcomes the\nproblems commonly encountered with electronic file sharing.\n Anyone, anywhere can open a PDF file. All you need is the free Adobe Acrobat\nReader. Recipients of other file formats sometimes can't open files because they\ndon't have the applications used to create the documents.\n PDF files \nalways print correctly\n on any printing device.\n PDF files always display \nexactly\n as created, regardless of fonts, software, and\noperating systems. Fonts, and graphics are not lost due to platform, software, and\nversion incompatibilities.\n The free Acrobat Reader is easy to download and can be freely distributed by\nanyone.\n Compact PDF files are smaller than their source files and download a\npage at a time for fast display on the Web.\n"
    },
    {
      "Date Time Updated": "not available",
      "Date Time Uploaded": "2021-03-29 03:11:13.387535",
      "File Name": "PDFtest.pdf",
      "Name": "3e",
      "TextExtracted": "  PDF Test File  Congratulations, your computer is equipped with a PDF (Portable Document Format) reader!  You should be able to view any of the PDF documents and forms available on our site.  PDF forms are indicated by these icons: \n  or  \n.    Yukon Department of Education Box 2703 Whitehorse,Yukon Canada Y1A 2C6  Please visit our website at:  \nhttp://www.education.gov.yk.ca/\n   "
    }
  ]
  ```
---
2.3 *Update the name of the file stored on mongoDB extracted data (U)*
  * Update file name and also update with the time when a file is updated
  * Upon successful operation, redirect back to retrieve_text. Return json containing 5 parameters with new 'date time updated'

  URI  | HTTP Method
  ------------- | -------------
  /uploader/retrieve-text/(oldname)/update/(newname) | GET
  /uploader/retrieve-text/(name) | GET

  **Successful response example**
  ```json
  [
    {
      "Date Time Updated": "2021-03-29 08:23:08.908766",
      "Date Time Uploaded": "2021-03-29 08:13:46.738869",
      "File Name": "PDFtest.pdf",
      "Name": "5e",
      "TextExtracted": "  PDF Test File  Congratulations, your computer is equipped with a PDF (Portable Document Format) reader!  You should be able to view any of the PDF documents and forms available on our site.  PDF forms are indicated by these icons: \n  or  \n.    Yukon Department of Education Box 2703 Whitehorse,Yukon Canada Y1A 2C6  Please visit our website at:  \nhttp://www.education.gov.yk.ca/\n   "
    }
  ]
  ```
---
2.4 *Delete file(s) stored on mongoDB extracted_data (D)*
  * User can delete one file by specifying the name of the file in URI
  * User can also delete all the files stored in mongoDB extracted_data collection
  * Upon successful operation, user will be shown with 'deleted successfully'

  URI  | HTTP Method
  ------------- | -------------
  /uploader/retrieve-text/delete-many/(name) | GET
  /uploader/retrieve-text/delete-all | GET

  **Successful response example**
  ```json
  {
    "result": "Deleted successfully"
  }
  ```

## Log data
**Logging** was included in the API with the following format:
> '[%(levelname)s] %(asctime)s %(message)s'

This was included to help user see the response from the API with timestamp. levelname can include info, debug, error etc. Use this logging data to debug. When running API, uploader.log file will be generated within the same directory.
