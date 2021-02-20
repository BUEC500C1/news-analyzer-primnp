# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom

## User Stories - Secure File Uploader/Ingester
*  As a user, I want to upload local file to database
*  As a user, I want to upload various file types with different formatting
*  As a user, I want to cancel my uploaded file while  it is in progress
*  As a user, I want to see the progress of the upload whether there are any issues or the task has been completed
*  As a user, I want to re-upload files when uploading fails
*  As a user, I want to convert between file types
*  As a user, I want to have a secure uploading process
*  As a user, I want to upload more than one file at a time
*  As a user, I want to control who has access to my files
*  As a user, I want to view/edit/delete files I have uploaded

>  Entity-based module


## JSON requests and responses
1. Ingesting data from uploaded files (Create)

URI  | HTTP Method
------------- | -------------
/file  | POST

#### Successful upload response
```JSON
{
  "File_URL": "file_url",
  "ID": "/file_url/User_ID/File_ID",
  "File_Metadata": {
    "Author": "author name",
    "Timestamps": "time_stamps",
    "File_source": "file_source",
    "Original_tags": "original_tags",
    "File_type": "file_type"
  },
  "Text_Fields": {
    "Text_ID": "text_ID",
    "Text": "text_attributes",
    "Sentiment": "file_sentiments",
    "NLP": ["test", "test2"]
  },
  "File_Info": {
    "File_name": "file_name",
    "File_ID": "File_ID",
    "User_ID": "user_ID",
    "Created_time":  "created_time",
    "Permissions": ["user_ID", "user_ID"],
    "Time_modified": "time_mod",
    "File_tags": "file_tags",
    "File_type": "file_type",
    "Notes":  "notes"
  }
}
```

### Unsuccessful upload response
* Follows HTTP Status code; below is an example of client error - request timeout
```JSON
{
  "err": {
    "code": 408,
    "message": "Request Timeout"
  },
  "status": "fail"
}
```

2. Modifying data from uploaded file (Update)

URI  | HTTP Method
------------- | -------------
/file/File_Info | PUT
```JSON
{
  "User_ID": "user_ID",
  "Created_time":  "created_time",
  "Permissions": ["user_ID", "user_ID"],
  "Time_modified": "time_mod",
  "File_tags": "file_tags",
  "File_type": "file_type",
  "Notes":  "notes"
}
```

#### Successful modify response
```JSON
{
  "File_URL": "file_url",
  ...
}
```
#### Unsuccessful modify response
* Follows HTTP Status code; below is an example of client error - forbidden
```JSON
{
  "err": {
    "code": 403,
    "message": "Forbidden"
  },
  "status": "fail"
}
```

3. Create user

URI  | HTTP Method
------------- | -------------
/user | POST
```JSON
{
  "User_ID": "user_ID",
  "name":  "my_username",
  "First_name": "My",
  "Last_name": "Username",
  "Display_name": "My Username",
  "Email": "myusername@example.test",
  "Password":  {
    "value": "password"
  },
  "Active":  true
}
```
