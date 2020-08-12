from typing import List, Union, TypedDict

from twitter.api_client import TwitterRawApi
from twitter.endpoints.users.friendship_models import FriendshipUserWithStatus
from twitter.endpoints.users.models import (
    TwitterUser,
    UserCursorList,
    TwitterRelationship,
)
from twitter.models.cursor import IDCursorList
from twitter.paths import PathOperation
from twitter.utils import check_id_or_screen_name, check_ids_or_screen_names

USERS_PATH = PathOperation("/users")
LOOKUP_PATH = USERS_PATH + "/lookup.json"
SEARCH_PATH = USERS_PATH + "/search.json"
SHOW_PATH = USERS_PATH + "/show.json"
FOLLOWERS_PATH = PathOperation("/followers")
FOLLOWERS_IDS_PATH = FOLLOWERS_PATH + "/ids.json"
FOLLOWERS_LIST_PATH = FOLLOWERS_PATH + "/list.json"
FRIENDS_PATH = PathOperation("/friends")
FRIENDS_ID_PATH = FRIENDS_PATH + "/ids.json"
FRIENDS_LIST_PATH = FRIENDS_PATH + "/list.json"
FRIENDSHIPS_PATH = PathOperation("/friendships")
FRIENDSHIPS_INCOMING_PATH = FRIENDSHIPS_PATH + "/incoming.json"
FRIENDSHIPS_LOOKUP_PATH = FRIENDSHIPS_PATH + "/lookup.json"
FRIENDSHIPS_NO_RETWEETS_PATH = FRIENDSHIPS_PATH + "/no_retweets"
FRIENDSHIPS_NO_RETWEETS_IDS_PATH = FRIENDSHIPS_NO_RETWEETS_PATH + "/ids.json"
FRIENDSHIPS_OUTGOING_PATH = FRIENDSHIPS_PATH + "/outgoing.json"
FRIENDSHIPS_SHOW_PATH = FRIENDSHIPS_PATH + "/show.json"
FRIENDSHIPS_CREATE_PATH = FRIENDSHIPS_PATH + "/create.json"
FRIENDSHIPS_DESTROY_PATH = FRIENDSHIPS_PATH + "/destroy.json"
FRIENDSHIPS_UPDATE_PATH = FRIENDSHIPS_PATH + "/update.json"


class UserApi(TwitterRawApi):
    def lookup_user(
        self,
        screen_names: Union[List[str], str] = None,
        user_ids: Union[List[int], int] = None,
        include_entities: bool = False,
        tweet_mode: bool = False,
    ) -> List[TwitterUser]:
        screen_names, user_ids = check_ids_or_screen_names(screen_names, user_ids)
        return [
            TwitterUser.from_json(TwitterUser, v)
            for v in self.full_authenticated_request(
                "GET",
                LOOKUP_PATH,
                params={
                    "screen_name": ",".join(screen_names),
                    "user_id": ",".join(user_ids),
                    "include_entities": include_entities,
                    "tweet_mode": tweet_mode,
                },
            )
        ]

    def search_user(
        self, q: str, page: int = 3, count: int = 5, include_entities: bool = False
    ) -> List[TwitterUser]:
        return [
            TwitterUser.from_json(TwitterUser, v)
            for v in self.full_authenticated_request(
                "GET",
                SEARCH_PATH,
                params={
                    "q": q,
                    "page": page,
                    "count": count,
                    "include_entities": include_entities,
                },
            )
        ]

    def show_user(
        self,
        screen_name: str = None,
        user_id: int = None,
        include_entities: bool = False,
    ) -> TwitterUser:
        check_id_or_screen_name(screen_name, user_id)
        return TwitterUser.from_json(
            TwitterUser,
            self.full_authenticated_request(
                "GET",
                SHOW_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "include_entities": include_entities,
                },
            ),
        )


class FriendsFollowersApi(TwitterRawApi):
    def get_follower_ids(
        self,
        screen_name: str = None,
        user_id: int = None,
        cursor: int = -1,
        stringify_ids: bool = False,
        count: int = None,
    ) -> IDCursorList:
        check_id_or_screen_name(screen_name, user_id)
        return IDCursorList.from_json(
            IDCursorList,
            self.full_authenticated_request(
                "GET",
                FOLLOWERS_IDS_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "cursor": cursor,
                    "stringify_ids": stringify_ids,
                    "count": count,
                },
            ),
        )

    def get_followers_list(
        self,
        screen_name: str = None,
        user_id: int = None,
        cursor: int = -1,
        count: int = None,
        skip_status: bool = False,
        include_user_entities: bool = True,
    ) -> UserCursorList:
        return UserCursorList.from_json(
            UserCursorList,
            self.full_authenticated_request(
                "GET",
                FOLLOWERS_LIST_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "cursor": cursor,
                    "count": count,
                    "skip_status": skip_status,
                    "include_user_entities": include_user_entities,
                },
            ),
        )

    def get_friend_ids(
        self,
        screen_name: str = None,
        user_id: int = None,
        cursor: int = -1,
        stringify_ids: bool = False,
        count: int = None,
    ) -> IDCursorList:
        check_id_or_screen_name(screen_name, user_id)
        return IDCursorList.from_json(
            IDCursorList,
            self.full_authenticated_request(
                "GET",
                FRIENDS_ID_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "cursor": cursor,
                    "stringify_ids": stringify_ids,
                    "count": count,
                },
            ),
        )

    def get_friends_list(
        self,
        screen_name: str = None,
        user_id: int = None,
        cursor: int = -1,
        count: int = None,
        skip_status: bool = False,
        include_user_entities: bool = True,
    ) -> UserCursorList:
        return UserCursorList.from_json(
            UserCursorList,
            self.full_authenticated_request(
                "GET",
                FRIENDS_LIST_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "cursor": cursor,
                    "count": count,
                    "skip_status": skip_status,
                    "include_user_entities": include_user_entities,
                },
            ),
        )

    def get_incoming_friendships(
        self, cursor: int = None, stringify_ids: bool = False
    ) -> IDCursorList:
        return IDCursorList.from_json(
            IDCursorList,
            self.full_authenticated_request(
                "GET",
                FRIENDSHIPS_INCOMING_PATH,
                params={"cursor": cursor, "stringify_ids": stringify_ids},
            ),
        )

    def lookup_friendships(
        self,
        screen_names: Union[List[str], str] = None,
        user_ids: Union[List[int], int] = None,
    ) -> List[TwitterUser]:
        screen_names, user_ids = check_ids_or_screen_names(screen_names, user_ids)

        return [
            TwitterUser.from_json(TwitterUser, v)
            for v in self.full_authenticated_request(
                "GET",
                FRIENDSHIPS_LOOKUP_PATH,
                params={
                    "screen_name": ",".join(screen_names),
                    "user_id": ",".join(user_ids),
                },
            )
        ]

    def get_no_retweets_friendship_ids(self, stringify_ids: bool = False) -> List[str]:
        return self.full_authenticated_request(
            "GET",
            FRIENDSHIPS_NO_RETWEETS_IDS_PATH,
            params={"stringify_ids": stringify_ids},
        )

    def get_outgoing_friendship_ids(
        self, cursor: int = -1, stringify_ids=False
    ) -> IDCursorList:
        return IDCursorList.from_json(
            IDCursorList,
            self.full_authenticated_request(
                "GET",
                FRIENDSHIPS_OUTGOING_PATH,
                params={"cursor": cursor, "stringify_ids": stringify_ids},
            ),
        )

    def show_friendship(
        self,
        source_screen_name=None,
        source_id=None,
        target_screen_name=None,
        target_id=None,
    ):
        check_id_or_screen_name(source_screen_name, source_id)
        check_id_or_screen_name(target_screen_name, target_id)
        return TwitterRelationship.from_json(
            TwitterRelationship,
            self.full_authenticated_request(
                "GET",
                FRIENDSHIPS_SHOW_PATH,
                params={
                    "source_id": source_id,
                    "source_screen_name": source_screen_name,
                    "target_id": target_id,
                    "target_screen_name": target_screen_name,
                },
            )["relationship"],
        )

    def create_friendships(
        self, screen_name: str = None, user_id: int = None, follow: bool = True
    ) -> FriendshipUserWithStatus:
        check_id_or_screen_name(screen_name, user_id)
        return FriendshipUserWithStatus.from_json(
            FriendshipUserWithStatus,
            self.full_authenticated_request(
                "POST",
                FRIENDSHIPS_CREATE_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "follow": follow,
                },
            ),
        )

    def destroy_friendship(
        self, screen_name: str = None, user_id: int = None
    ) -> FriendshipUserWithStatus:
        check_id_or_screen_name(screen_name, user_id)
        return FriendshipUserWithStatus.from_json(
            FriendshipUserWithStatus,
            self.full_authenticated_request(
                "POST",
                FRIENDSHIPS_DESTROY_PATH,
                params={"screen_name": screen_name, "user_id": user_id},
            ),
        )

    def update_friendship(
        self,
        screen_name: str = None,
        user_id: int = None,
        device: bool = None,
        retweets: bool = False,
    ) -> TwitterRelationship:
        return TwitterRelationship.from_json(
            TwitterRelationship,
            self.full_authenticated_request(
                "POST",
                FRIENDSHIPS_UPDATE_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "device": device,
                    "retweets": retweets,
                },
            ),
        )
