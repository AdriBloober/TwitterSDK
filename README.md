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

### How to get the authentication credentials?

Go here (https://developer.twitter.com/en/apps) and create a developer app. Under Tab `Keys and tokens` get you'r tokens.

```python
from twitter.api import TwitterApi

consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

api = TwitterApi(consumer_key, consumer_secret, access_token_key, access_token_secret)
```

The `TwitterApi` object contains all methods.
