# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom

## User Stories - News Feed Ingester
* As a user, I want to upload/organize news feed to database
* As a user, I want to discover content from web to enhance story
* As a user, I want to know the source of the articles
* As a user, I want to find the common keywords inside my files
* As a user, I want to create link between keywords in the ingested and discovered content
* As a user, I want to find sentiment of the content
* As a user, I want to search based on keywords and sentiment
* As a user, I want to analyze keywords which relate to sentiments

> Procedure-base module

## Functions - Actions that need to be completed
* file = ingestFile()
* NameFile(file, name)
* GetFileData(file)
* UpdateFile(file)
* KeywordsSearch = searchOnKeywords()
* SentimentSearch = searchOnSentiment()
* GetSearchData(KeywordsSearch) or GetSearchData(SentimentSearch)
* FileSource = findFileSource()
* GetFileSource(FileSource)
* CommonKeywords = searchCommonKeywords()
* ContentSentiment = findContentSentiment()
* KeywordsSentiment = linkKeywordsandSentiment()
* GetKeywordsSentimentData(KeywordSentiment)
* SearchResultandUploadedContent = linkSearchResultandUploadedContent()
* GetKeywordsLink(SearchResultandUploadedContent)
* RemoveCommonKeywords(CommonKeywords, file)
* RemoveContentSentiment(ContentSentiment, file)


## Example data
* File
  * File URL
  * MetaData
    * Author
    * Timestamps
    * File source
    * Original Tags
    * File type
  * Text_Fields
    * Text ID
    * Text
    * Sentiment
    * NLP
    * Keywords
  * File_content
    * File Name
    * User ID
    * Created Time
    * Permissions
    * Time modified
    * File Tags
    * File Type
    * Notes


## Operations
* Create
  * ingestFile(File)
* Delete
  * Delete(File.Text_Fields, Keywords)
  * Delete(File.Text_Fields, Sentiment)
* Read
  * File.MetaData, File source
  * File.Text_Fields, Sentiment
  * File.Text_Fields, Text
  * File.Text_Fields, Keywords
* Update
  * File.Text_Fields, Keywords
  * File.Text_Fields, Sentiment
  * File.File_content, Similar File URL
  * File.File_content, File Name
