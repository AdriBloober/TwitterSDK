from typing import List

from twitter.endpoints.users.models import TwitterUser
from twitter.models import TwitterModel
from twitter.models.datetime import TwitterDatetime
from twitter.models.entities import TwitterEntities
from twitter.models.geo import TwitterCoordinates, TwitterPlaces


class TwitterRule(TwitterModel):
    tag: str
    id: int
    id_str: str


class TwitterStatusTweet(TwitterModel):
    id: int
    id_str: str
    created_at: TwitterDatetime
    text: str
    source: str
    truncated: bool
    in_reply_to_status_id: int
    in_reply_to_status_id_str: str
    in_reply_to_user_id: int
    in_reply_to_user_id_str: str
    in_reply_to_screen_name: str
    user: TwitterUser
    coordinates: TwitterCoordinates
    place: TwitterPlaces
    quoted_status_id: int
    quoted_status_id_str: str
    is_quote_status: bool
    quote_count: int
    reply_count: int
    retweet_count: int
    favorite_count: int
    entities: TwitterEntities
    extended_entities: TwitterEntities
    favorited: bool
    retweeted: bool
    possibly_sensitive: bool
    filter_level: str
    lang: str
    matching_rules: List[TwitterRule]
    __extra_annotations__ = {
        "quoted_status": "TwitterStatusTweet",
        "retweeted_status": "TwitterStatusTweet",
    }


class TwitterSearchMetadata(TwitterModel):
    completed_in: float
    max_id: int
    max_id_str: str
    next_results: str
    query: str
    count: int
    since_id: int
    since_id_str: str


class TwitterSearchResponse(TwitterModel):
    statuses: List[TwitterStatusTweet]
    search_metadata: TwitterSearchMetadata


class TwitterOEmbed(TwitterModel):
    url: str
    author_name: str
    author_url: str
    html: str
    width: int
    height: int
    type: str
    cache_age: str
    provider_name: str
    provider_url: str
    version: str
