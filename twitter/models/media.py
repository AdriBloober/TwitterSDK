from typing import List

from twitter.models import TwitterModel


class TwitterSize(TwitterModel):
    w: int
    h: int
    resize: str


class TwitterSizes(TwitterModel):
    thumb: TwitterSize
    large: TwitterSize
    medium: TwitterSize
    small: TwitterSize


class TwitterMediaObject(TwitterModel):
    display_url: str
    expanded_url: str
    id: int
    id_str: str
    indices: List[int]
    media_url: str
    media_url_https: str
    sizes: TwitterSizes
    source_status_id: int
    source_status_id_str: str
    type: str
    url: str
