import json

def uploader(x):
    py2Json = json.dumps(x)
    return py2Json

#test
# if __name__ == '__main__':
#     #a = {'name':'Sarah', 'age': 24, 'isEmployed': True }
#     a = {
#       "File_URL": "https://example.test/testart",
#       "ID": "/https://example.test/testart/001/0120",
#       "File_Metadata": {
#         "Author": "ABC DEF",
#         "Timestamps": "4:00PM",
#         "File_source": "Github",
#         "Original_tags": ["Educational", "Politics"],
#         "File_type": "pdf"
#       },
#       "Text_Fields": {
#         "Text_ID": "011",
#         "Text": "a very very very long text",
#         "Sentiment": "Positive",
#         "NLP": ["test", "test2"]
#       },
#       "File_Info": {
#         "File_name": "file_name",
#         "User_ID": "user_ID",
#         "Created_time":  "created_time",
#         "Permissions": ["user_ID", "user_ID"],
#         "Time_modified": "time_mod",
#         "File_tags": "file_tags",
#         "File_type": "file_type",
#         "Notes":  "notes"
#       }
#     }
#     test = uploader(a)
#     print(test)
