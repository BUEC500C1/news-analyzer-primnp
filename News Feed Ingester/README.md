# news-analyzer-primnp
news-analyzer-primnp created by GitHub Classroom

## User Stories - News Feed Ingester
* As a user, I want to discover more news feed to enhance my web content
* As a user, I want to know the source of the articles
* As a user, I want to search for articles using key words
* As a user, I want to search articles based on month, date, and year
* As a user, I want to view suggested news article based on my recent searches
* As a user, I want to keep track of log information for debugging

> Procedure-base module

## Build Instructions
Aside from cloning the repo, there are several steps that needs to be implemented. Start by installing pynytimes library
```
pip install --upgrade pynytimes
```
Then follow https://pypi.org/project/pynytimes/. You also need to create NYTimes developer account (https://developer.nytimes.com/my-apps/60ca4fa5-f5e6-4372-ab87-6555c58f71d8) to get your API key and use the key for this API implementation.
```Python
nyt = NYTAPI("Your API key", parse_dates=True)
```

## API Requests & Responses

For this API implementation, I created three main function.

1. **findWithKeyword(string: keyword)**
  * take in string parameter
  * find articles using NYT article search API with 'keyword' as a query. Return snippet, web url, and source of articles found (these schema can be changed, refer to: https://developer.nytimes.com/docs/articlesearch-product/1/types/Article)
  * Note: I set the NYT API to return 10 results per one keyword. This is because the results variable is limited to multiple of 10


URI  | HTTP Method
------------- | -------------
/newsfeedig/onequery/(keyword)  | GET

#### Successful operation response example
```JSON
{"News Feed Results":[{
  "Snippet":"New York City, long buoyed by the flow of commuters into its towering office buildings, faces a cataclysmic challenge, even when the pandemic ends.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/29/nyregion/remote-work-coronavirus-pandemic.html"},{
  "Snippet":"Yes, tech companies are hiring. Here\u2019s why they want you to notice.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/23/technology/big-tech-jobs-politics.html"},{
  "Snippet":"Antitrust bills would dismantle Apple and Google\u2019s monopoly over the distribution of smartphone apps and entice companies to relocate to those states.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/18/opinion/apple-google-app-monopoly.html"},{
  "Snippet":"Loretta Staples, a U.I. designer in the 1980s and \u201990s, had a front-row seat to the rise of personal computing.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/18/style/loretta-staples-ui-design.html"},{
  "Snippet":"Google said that starting July 1, it would take 15 percent of the first $1 million developers take in from certain app sales, down from 30 percent.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/16/business/google-play-developer-fees.html"},{
  "Snippet":"The 10 percent threshold for a correction is arbitrary, but it is often an indication that investors have turned more pessimistic about the markets.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/04/business/nasdaq-tech-stocks-correction.html"},{
  "Snippet":"Don\u2019t want to pay $1,900 for a Peloton bike, plus a subscription fee for classes? Here are ways to reduce the cost of using tech to exercise at home.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/03/technology/personaltech/peloton-alternatives-at-home-workout.html"},{
  "Snippet":"Every month, streaming services add a new batch of titles to their libraries. Here are our picks for March.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/02/arts/best-movies-tv-hulu-disney.html"},{
  "Snippet":"The change, for now only visible to beta testers, reflects the popularity and shifting meaning of a symbol once mainly used to discuss blood donations.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/02/18/world/apple-syringe-emoji-coronavirus-vaccine.html"},{
  "Snippet":"Where\u2019s \u201cSuccession\u201d? \u201cAtlanta\u201d? After the number of scripted shows fell for the first time in a decade, Hollywood hopes to satisfy a restless audience with less costly fare.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/02/28/business/media/pandemic-streaming-tv-shows.html"
  }]
}
```
#### Failed operation response - empty string
```JSON
{"News Feed Results":[]}
```
---
2. **findWithKeywordLists(string: keyword-keyword-keyword-.....)**
  * take in several keywords as string parameter separated by '-'
  * find articles using NYT article search API with all the keywords as query. Return snippet, web url, and source of articles found (these schema can be changed, refer to: https://developer.nytimes.com/docs/articlesearch-product/1/types/Article)
  * Note: I set the NYT API to return 10 results per one keyword. This is because the results variable is limited to multiple of 10


URI  | HTTP Method
------------- | -------------
/newsfeedig/listquery/(keyword-keyword-keyword....)  | GET

#### Successful operation response example
```json
{"News Feed Results":[{
  "Snippet":"New York City, long buoyed by the flow of commuters into its towering office buildings, faces a cataclysmic challenge, even when the pandemic ends.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/29/nyregion/remote-work-coronavirus-pandemic.html"},{
  "Snippet":"Yes, tech companies are hiring. Here\u2019s why they want you to notice.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/23/technology/big-tech-jobs-politics.html"},{
  "Snippet":"Antitrust bills would dismantle Apple and Google\u2019s monopoly over the distribution of smartphone apps and entice companies to relocate to those states.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/18/opinion/apple-google-app-monopoly.html"},
  ...
  }]
}
```
#### Failed operation response - empty string
```JSON
{"News Feed Results":[]}
```
---
3. **findWithDMY(year2, year1, month2, month1, day2, day1, keywords)**
  * take in start and end day, month, year and several keywords (separate by '-') as string parameters
  * find articles using NYT article search API with parameters stated above as query. Return snippet, web url, and source of articles found (these schema can be changed, refer to: https://developer.nytimes.com/docs/articlesearch-product/1/types/Article)
  * Note: I set the NYT API to return 10 results per one keyword. This is because the results variable is limited to multiple of 10

URI  | HTTP Method
------------- | -------------
/newsfeedig/dmyquery/year1=(string:year1)&month1=(string:month1)&day1=(string:day1)&year2=(string:year2)&month2=(string:month2)&day2=(string:day2)&keywords=(string:keywords)  | GET

#### Successful operation response example
```json
{"News Feed Results":[{
  "Snippet":"Beyonc\u00e9 broke a record, Megan Thee Stallion and H.E.R. won awards, Taylor Swift\u2019s \u201cFolklore\u201d was named album of the year and Billie Eilish\u2019s \u201cEverything I Wanted\u201d record of the year.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/14/arts/music/grammy-awards-beyonce-taylor-swift.html"},{
  "Snippet":"Half the country has been inoculated, ushering in a kind of normalcy that is largely defined by the people it excludes.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/15/podcasts/the-daily/israel-vaccinations-coronavirus.html"},{    "Snippet":"The two men are up for supporting actor in \u201cJudas and the Black Messiah,\u201d a best picture candidate. So who was the star? And the Globes\u2019 best supporting actress was shut out.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/15/movies/oscars-snubs-surprises.html"},{
  "Snippet":"Most of the top contenders can be watched at home. Here\u2019s a guide to help you get a jump on the field.","Source":"The New York Times","WebURL":"https://www.nytimes.com/2021/03/15/movies/stream-oscars-nominated-movies.html"},
  ...
  }]
}
```

#### Failed operation response - empty string
```JSON
{"News Feed Results":null}
```

## Log data
**Logging** was included in the API with the following format:
> '[%(levelname)s] %(asctime)s %(message)s'

This was included to help user see the response from the API with timestamp. levelname can include info, debug, error etc. Use this logging data to debug. When running API, newsfeed.log file will be generated within the same directory.
