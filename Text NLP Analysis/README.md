# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom


## User Stories - Text NLP Analysis
* As a user, I want to find text's entities
* As a user, I want to find text's sentiment
* As a user, I want to know category of the text
* As a user, I want to obtain keywords from text
* As a user, I want to input keywords/text to get sentiment
* As a user, I want to know possible (entities,sentiments) key value pair

> Procedure-based module

## Build Instructions
You will need a google cloud account. After setting up google cloud account, follow https://cloud.google.com/natural-language/docs/setup to set up Google NLP API. This includes: setting up credentials, download private-key file, and use the service account key file in your environment etc.
```
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/my-key.json"
```
We will use key file to make request such as POST https://oauth2.googleapis.com/token

## API Requests & Responses

1. **analyze_sentiment(string: text)**
  * take in string parameter
  * analyze sentiment of the given text string

URI  | HTTP Method
------------- | -------------
/nlp/retrieve-sentiment/(text)  | GET

#### Successful operation response example
```JSON
[
  {
    "SentimentScore":-0.7800000023841847,
    "TextInput":"A quick brown fox jumps over a lazy dog. The lazy dog then disappear mysteriously."
  }
]
```
#### Failed operation response - empty string
```JSON
{"SentimentScore":[]}
```

2. **analyze_entities(string: text)**
  * take in string parameter
  * analyze entities of the given text string

  URI  | HTTP Method
  ------------- | -------------
  /nlp/retrieve-entity/(text) | GET

#### Successful operation response example
```JSON
[
  {
    "Entities":["dog","brown fox"],
    "TextInput":"A quick brown fox jumps over a lazy dog. The lazy dog then disappear mysteriously."
  }
]
```
#### Failed operation response - empty string
```JSON
{"Entities":[]}
```

3. **analyze_entities_sentiments(string: text)**
  * take in string parameter
  * analyze (entities, sentiments) value pair of the given text string

URI  | HTTP Method
------------- | -------------
/nlp/retrieve-entity-sentiment/(text)  | GET

#### Successful operation response example
```JSON
{
  "Results": [{
      "Entity":"dog","Score":-0.05000000074505806},{
      "Entity":"brown fox","Score":0.0
      }
  ]
}

```
#### Failed operation response - empty string
```JSON
{"Results":[]}
```

4. **classify_content(string: text)**
  * take in string parameter
  * classify the given text into possible categories

URI  | HTTP Method
------------- | -------------
/nlp/content-classification/(text) | GET

#### Successful operation response example
```JSON
{
  "Results":[{
      "Category":"/Arts & Entertainment","Score":0.6100000143051147 },{
      "Category":"/Pets & Animals","Score":0.5799999833106995},{
      "Category":"/Hobbies & Leisure","Score":0.5
    }
  ]
}
```
#### Failed operation response - empty string
```JSON
{"Results":[]}
```


## Log data
**Logging** was included in the API with the following format:
> '[%(levelname)s] %(asctime)s %(message)s'

This was included to help user see the response from the API with timestamp. levelname can include info, debug, error etc.
When running API, nlp.log file will be generated within the same directory.
