from twitter.endpoints.tweets.api import TweetsApi
from twitter.endpoints.users.api import UserApi, FriendsFollowersApi


class TwitterApi(UserApi, FriendsFollowersApi, TweetsApi):
    """TwitterAPI with subapi's."""

    pass
