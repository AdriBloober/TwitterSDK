from twitter.endpoints.users.api import UserApi, FriendsFollowersApi


class TwitterApi(UserApi, FriendsFollowersApi):
    """TwitterAPI with subapi's."""

    pass
