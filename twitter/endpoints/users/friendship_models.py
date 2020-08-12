from twitter.endpoints.tweets.models import TwitterStatusTweet
from twitter.endpoints.users.models import TwitterUser


class FriendshipUserWithStatus(TwitterUser):
    status: TwitterStatusTweet
