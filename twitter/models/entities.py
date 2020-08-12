from typing import List

from twitter.models import TwitterModel
from twitter.models.datetime import TwitterDatetime
from twitter.models.media import TwitterMediaObject


class TwitterHashtag(TwitterModel):
    indices: List[int]
    text: str


class TwitterURL(TwitterModel):
    display_url: str
    expanded_url: str
    indices: List[int]
    url: str


class UserMentionObject(TwitterModel):
    id: int
    id_str: str
    indices: List[int]
    name: str
    screen_name: str


class TwitterSymbol(TwitterModel):
    indices: List[int]
    text: str


class TwitterPollOption(TwitterModel):
    position: int
    text: str


class TwitterPollObject(TwitterModel):
    options: List[TwitterPollOption]
    end_datetime: TwitterDatetime
    duration_minutes: str


class TwitterEntities(TwitterModel):
    hashtags: List[TwitterHashtag]
    media: List[TwitterMediaObject]
    urls: List[TwitterURL]
    user_mentions: List[UserMentionObject]
    symbols: List[TwitterSymbol]
    polls: List[TwitterPollObject]
