from typing import List

from twitter.models.__init__ import TwitterModel
from twitter.models.datetime import TwitterDatetime


class TwitterUser(TwitterModel):
    id: int
    id_str: str
    name: str
    screen_name: str
    location: str
    url: str
    description: str
    protected: bool
    verified: bool
    followers_count: int
    listed_count: int
    favourites_count: int
    statuses_count: int
    created_at: TwitterDatetime
    profile_banner_url: str
    profile_image_url_https: str
    default_profile: bool
    default_profile_image: bool
    withheld_in_countries: List[str]
    withheld_scope: str


class UserCursorList(TwitterModel):
    users: List[TwitterUser]
    next_cursor: int
    next_cursor_str: str
    previous_cursor: int
    previous_cursor_str: str


class SourceRelationship(TwitterModel):
    id: int
    id_str: str
    screen_name: str
    following: bool
    followed_by: bool
    live_following: bool
    can_dm: bool


class TargetRelationship(TwitterModel):
    id: int
    id_str: str
    screen_name: str
    following: bool
    followed_by: bool


class TwitterRelationship(TwitterModel):
    source: SourceRelationship
    target: TargetRelationship
