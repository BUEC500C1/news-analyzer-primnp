# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom


##User Stories - Text NLP Analysis
* As a user, I want to search using keywords and boolean operators
* As a user, I want to identify repeated phrase/keywords throughout documents
* As a user, I want to create links with other documents via common keywords
* As a user, I want to get recommendations based off previous search
* As a user, I want to translate a word into another language (?)
* As a user, I want to input keywords/text to get sentiment
* As a user, I want to search keywords and get relevant information from the web
* As a user, I want to find bias of documents based on keywords/phrases
* As a user, I want to extract and classify text data (e.g, emails, product reviews, tweets)

> Procedure-based module

##Functions - Actions that need to be completed
* KeywordsSearch = searchOnKeywords()
* BooleanSearch = searchBoolean()
* RepeatedWords = searchRepeatedWords()
* CommonKeywords = searchCommonKeywords()
* LinkDocuments = linkDocViaKeywords()
* GetDocuments(LinkDocuments)
* SearchRecommendations = linkPreviousSearch()
* GetSearchHistory()
* TextTranslated = translateText()
* ContentSentiment = findContentSentiment()
* KeywordsSentiment = linkKeywordsandSentiment()
* GetFilesfromWeb(KeywordsSearch)
* BiasInfo = findBiasOnKeywords()
* DataClassifications = ClassifyDatas()
* UpdateBias(text)
* UpdateLanguage(text)
* RemoveBias = RemoveBiasData(BiasInfo, text)


##Example data
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
    * Keywords
      * Bias
      * Language
    * Bias
  * File_content
    * File Name
    * User ID
    * Created Time
    * Permissions
    * Time modified
    * File Tags
    * File Type
    * Notes


##Operations
* Create
  * Create bias, determine link between keywords, create translated text e.g.:
    * findBiasOnKeywords()
    * linkDocViaKeywords()
    * SearchRecommendations()
    * translateText()
    * findKeywordsSentiment()
    * searchOnKeywords()
    ...
* Delete
  * Delete(File.Text_Fields, Bias)
* Read
  * File.Text_Fields, Sentiment
  * File.Text_Fields, Text
  * File.Text_Fields, Keywords
  * File.Text_Fields, Bias
  * File.Text_Fields, Language
  * searchBoolean()
* Update
  * File.Text_Fields, Keywords, Bias
  * File.Text_Fields, Bias
  * File.File_content, Language
