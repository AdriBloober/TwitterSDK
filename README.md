# TwitterAPI (Python)

## Installation

This python package requires python >= 3.6 with pip.

### Install with pip

```shell
python3 -m pip install --upgrade --user twitter_sdk
```

### Install manual

```shell
git clone https://github.com/AdriBloober/TwitterSDK && cd TwitterSDK
python3 setup.py install
```

## How to use?

Go here (https://developer.twitter.com/en/apps) and create a developer app. Under Tab `Keys and tokens` get you'r tokens.


### How to get the authentication credentials? (OAuth1.0)


```python
from twitter.api import TwitterApi, TwitterAuth

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

api = TwitterApi(TwitterAuth.get_oauth1_auth(consumer_key, consumer_secret, access_token_key, access_token_secret))
```

### How to get the authentication credentials? (OAuth2-Bearer Token)
```python
from twitter.api import TwitterApi, TwitterAuth

bearer_token = ""

api = TwitterApi(TwitterAuth.get_oauth2_bearer_token(bearer_token))
```

### How to get the authentication credentials? (Basic Auth for premium & enterprise)
```python
from twitter.api import TwitterApi, TwitterAuth

email_address = ""
password = ""

api = TwitterApi(TwitterAuth.get_basic_authentication(email_address, password))
```

The `TwitterApi` object contains all methods.

### Rate limits

Here are all rate limits documented: https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits/endpoint-rate-limits.   
If the rate limit has been reached, the error ``twitter.error_management.RateLimitReachedError`` will been thrown.

### HTTPErrors

If the response status code is betweet 400 and 599, the ``twitter.error_management.TwitterError`` will been thrown.
```python
import requests
class TwitterError(Exception):
  status_message: str
  status_code: int
  url: str
  response: requests.Response
  def __init__(self, status_message, status_code, url, response=None):
    self.status_message = status_message
    self.status_code = status_code
    self.url = url
    self.response = response
    super().__init__(f"Error {status_code}: {status_message} for url {url}.")
```
