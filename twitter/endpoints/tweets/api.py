from datetime import datetime

from typing import Union, List

from twitter.api_client import TwitterRawApi
from twitter.endpoints.tweets.models import (
    TwitterSearchResponse,
    TwitterStatusTweet,
    TwitterOEmbed,
)
from twitter.models.cursor import IDCursorList
from twitter.paths import PathOperation
from twitter.utils import check_id_or_screen_name

SEARCH_PATH = PathOperation("/search")
SEARCH_TWEETS_PATH = SEARCH_PATH + "/tweets.json"
STATUSES_PATH = PathOperation("/statuses")
STATUSES_UPDATE_PATH = STATUSES_PATH + "/update.json"
DESTROY_STATUS_PATH = STATUSES_PATH + "/destroy"
SHOW_STATUS_PATH = STATUSES_PATH + "/show.json"
LOOKUP_STATUS_PATH = STATUSES_PATH + "/lookup.json"
RETWEET_STATUS_PATH = STATUSES_PATH + "/retweet"
UNRETWEET_STATUS_PATH = STATUSES_PATH + "/unretweet"
RETWEETS_STATUS_PATH = STATUSES_PATH + "/retweets"
RETWEETS_OF_ME_STATUS_PATH = STATUSES_PATH + "/retweets_of_me.json"
RETWEETERS_PATH = STATUSES_PATH + "/retweeters"
RETWEETERS_IDS_PATH = RETWEETERS_PATH + "/ids.json"
FAVORITES_PATH = PathOperation("/favorites")
FAVORITES_CREATE_PATH = FAVORITES_PATH + "/create.json"
FAVORITES_DESTROY_PATH = FAVORITES_PATH + "/destroy.json"
FAVORITES_LIST_PATH = FAVORITES_PATH + "/list.json"
HOME_TIMELINE_PATH = STATUSES_PATH + "/home_timeline.json"
USER_TIMELINE_PATH = STATUSES_PATH + "/user_timeline.json"
MENTIONS_TIMELINE_PATH = STATUSES_PATH + "/mentions_timeline.json"


class TweetsApi(TwitterRawApi):
    def search_tweets(
        self,
        q: str,
        geocode: str = None,
        lang: str = None,
        locale: str = None,
        result_type: str = None,
        count: int = None,
        until: datetime = None,
        since_id: int = None,
        max_id: int = None,
        include_entities: bool = False,
    ) -> TwitterSearchResponse:
        if until:
            until = datetime.strptime("%Y-%m-%d", until)

        return TwitterSearchResponse.from_json(
            TwitterSearchResponse,
            self.full_authenticated_request(
                "GET",
                SEARCH_TWEETS_PATH,
                params={
                    "q": q,
                    "geocode": geocode,
                    "lang": lang,
                    "locale": locale,
                    "result_type": result_type,
                    "count": count,
                    "until": until,
                    "since_id": since_id,
                    "max_id": max_id,
                    "include_entities": include_entities,
                },
            ),
        )

    def tweet(
        self,
        status: str,
        in_reply_to_status: TwitterStatusTweet = None,
        in_reply_to_status_id: int = None,
        auto_populate_reply_metadata: bool = False,
        exclude_reply_user_ids: Union[List[int], int] = None,
        attachment_url: str = None,
        media_ids: Union[List[int], int] = None,
        possibly_sensitive: bool = False,
        lat: float = None,
        long: float = None,
        place_id: int = None,
        display_coordinates: bool = None,
        trim_user: bool = False,
        enable_dmcommands: bool = False,
        fail_dmcommands: bool = True,
        card_uri: str = None,
    ) -> TwitterStatusTweet:
        if exclude_reply_user_ids and exclude_reply_user_ids != list:
            exclude_reply_user_ids = [exclude_reply_user_ids]
        if not exclude_reply_user_ids:
            exclude_reply_user_ids = []
        if media_ids and media_ids != list:
            media_ids = [media_ids]
        if not media_ids:
            media_ids = []
        if in_reply_to_status:
            in_reply_to_status_id = in_reply_to_status.id
        return TwitterStatusTweet.from_json(
            TwitterStatusTweet,
            self.full_authenticated_request(
                "POST",
                STATUSES_UPDATE_PATH,
                params={
                    "status": status,
                    "in_reply_to_status_id": in_reply_to_status_id,
                    "auto_populate_reply_metadata": auto_populate_reply_metadata,
                    "exclude_reply_user_ids": ",".join(exclude_reply_user_ids),
                    "attachment_url": attachment_url,
                    "media_ids": ",".join(media_ids),
                    "possibly_sensitive": possibly_sensitive,
                    "lat": lat,
                    "long": long,
                    "place_id": place_id,
                    "display_coordinates": display_coordinates,
                    "trim_user": trim_user,
                    "enable_dmcommands": enable_dmcommands,
                    "fail_dmcommands": fail_dmcommands,
                    "card_uri": card_uri,
                },
            ),
        )

    def delete_tweet(self, tweet_id: int, trim_user: bool = None) -> TwitterStatusTweet:
        return TwitterStatusTweet.from_json(
            TwitterStatusTweet,
            self.full_authenticated_request(
                "POST",
                DESTROY_STATUS_PATH + f"/{tweet_id}.json",
                params={"trim_user": trim_user},
            ),
        )

    def show_tweet_by_id(
        self,
        tweet_id: int,
        trim_user: bool = None,
        include_my_retweet: bool = None,
        include_entities: bool = None,
        include_ext_alt_text: bool = None,
        include_card_uri: bool = None,
    ) -> TwitterStatusTweet:
        return TwitterStatusTweet.from_json(
            TwitterStatusTweet,
            self.full_authenticated_request(
                "GET",
                SHOW_STATUS_PATH,
                params={
                    "id": tweet_id,
                    "trim_user": trim_user,
                    "include_my_retweet": include_my_retweet,
                    "include_entities": include_entities,
                    "include_ext_alt_text": include_ext_alt_text,
                    "include_card_uri": include_card_uri,
                },
            ),
        )

    def oembed(
        self,
        url: str,
        maxwidth: int = 325,
        hide_media: bool = False,
        hide_thread: bool = False,
        omit_script: bool = False,
        align: str = None,
        related: str = None,
        lang: str = None,
        theme: str = "light",
        link_color: str = None,
        widget_type: str = None,
    ) -> TwitterOEmbed:
        return TwitterOEmbed.from_json(
            TwitterOEmbed,
            self.full_authenticated_request(
                "GET",
                "https://publish.twitter.com/oembed",
                params={
                    "url": url,
                    "maxwidth": maxwidth,
                    "hide_media": hide_media,
                    "hide_thread": hide_thread,
                    "omit_script": omit_script,
                    "align": align,
                    "related": related,
                    "lang": lang,
                    "theme": theme,
                    "link_color": link_color,
                    "widget_type": widget_type,
                },
            ),
        )

    def lookup_tweet(
        self,
        user_ids: Union[List[int], int],
        include_entities: bool = None,
        trim_user: bool = None,
        map: bool = None,
        include_ext_alt_text: bool = None,
        include_card_uri: bool = None,
    ) -> List[TwitterStatusTweet]:
        if user_ids and type(user_ids) != list:
            user_ids = [user_ids]
        elif not user_ids:
            user_ids = []
        return [
            TwitterStatusTweet.from_json(TwitterStatusTweet, v)
            for v in self.full_authenticated_request(
                "GET",
                LOOKUP_STATUS_PATH,
                params={
                    "id": ",".join([str(user_id) for user_id in user_ids]),
                    "include_entities": include_entities,
                    "trim_user": trim_user,
                    "map": map,
                    "include_ext_alt_text": include_ext_alt_text,
                    "include_card_uri": include_card_uri,
                },
            )
        ]

    def retweet_tweet(
        self, tweet_id: int, trim_user: bool = None
    ) -> TwitterStatusTweet:
        return TwitterStatusTweet.from_json(
            TwitterStatusTweet,
            self.full_authenticated_request(
                "POST",
                RETWEET_STATUS_PATH + f"/{tweet_id}.json",
                params={"trim_user": trim_user},
            ),
        )

    def unretweet_tweet(
        self, tweet_id: int, trim_user: bool = None
    ) -> TwitterStatusTweet:
        return TwitterStatusTweet.from_json(
            TwitterStatusTweet,
            self.full_authenticated_request(
                "POST",
                UNRETWEET_STATUS_PATH + f"/{tweet_id}.json",
                params={"trim_user": trim_user},
            ),
        )

    def get_retweets(
        self, tweet_id: int, count: int = None, trim_user: bool = None
    ) -> List[TwitterStatusTweet]:
        return [
            TwitterStatusTweet.from_json(TwitterStatusTweet, v)
            for v in self.full_authenticated_request(
                "GET",
                RETWEETS_STATUS_PATH + f"/{tweet_id}.json",
                params={"count": count, "trim_user": trim_user},
            )
        ]

    def get_retweets_of_me(
        self,
        count: int = None,
        since_id: int = None,
        max_id: int = None,
        trim_user: bool = None,
        include_entities: bool = None,
        include_user_entities: bool = None,
    ) -> List[TwitterStatusTweet]:
        return [
            TwitterStatusTweet.from_json(TwitterStatusTweet, v)
            for v in self.full_authenticated_request(
                "GET",
                RETWEETS_OF_ME_STATUS_PATH,
                params={
                    "count": count,
                    "since_id": since_id,
                    "max_id": max_id,
                    "trim_user": trim_user,
                    "include_entities": include_entities,
                    "include_user_entities": include_user_entities,
                },
            )
        ]

    def get_retweeters_ids(
        self,
        tweet_id: int,
        count: int = None,
        cursor: int = None,
        stringify_ids: bool = None,
    ) -> IDCursorList:
        return IDCursorList.from_json(
            IDCursorList,
            self.full_authenticated_request(
                "GET",
                RETWEETERS_IDS_PATH,
                params={
                    "id": tweet_id,
                    "count": count,
                    "cursor": cursor,
                    "stringify_ids": stringify_ids,
                },
            ),
        )

    def like_tweet(
        self, tweet_id: int, include_entities: bool = None
    ) -> TwitterStatusTweet:
        return TwitterStatusTweet.from_json(
            TwitterStatusTweet,
            self.full_authenticated_request(
                "POST",
                FAVORITES_CREATE_PATH,
                params={"id": tweet_id, "include_entities": include_entities},
            ),
        )

    def unlike_tweet(
        self, tweet_id: int, include_entities: bool = None
    ) -> TwitterStatusTweet:
        return TwitterStatusTweet.from_json(
            TwitterStatusTweet,
            self.full_authenticated_request(
                "POST",
                FAVORITES_DESTROY_PATH,
                params={"id": tweet_id, "include_entities": include_entities},
            ),
        )

    def list_likes(
        self,
        screen_name: str = None,
        user_id: int = None,
        count: int = None,
        since_id: int = None,
        max_id: int = None,
        include_entities: bool = None,
    ) -> List[TwitterStatusTweet]:
        check_id_or_screen_name(screen_name, user_id)
        return [
            TwitterStatusTweet.from_json(TwitterStatusTweet, v)
            for v in self.full_authenticated_request(
                "GET",
                FAVORITES_LIST_PATH,
                params={
                    "screen_name": screen_name,
                    "user_id": user_id,
                    "count": count,
                    "since_id": since_id,
                    "max_id": max_id,
                    "include_entities": include_entities,
                },
            )
        ]

    def get_home_timeline(
        self,
        count: int = None,
        since_id: int = None,
        max_id: int = None,
        trim_user: bool = None,
        exclude_replies: bool = None,
        include_entities: bool = None,
    ) -> List[TwitterStatusTweet]:
        return [
            TwitterStatusTweet.from_json(TwitterStatusTweet, v)
            for v in self.full_authenticated_request(
                "GET",
                HOME_TIMELINE_PATH,
                params={
                    "count": count,
                    "since_id": since_id,
                    "max_id": max_id,
                    "trim_user": trim_user,
                    "exclude_replies": exclude_replies,
                    "include_entities": include_entities,
                },
            )
        ]

    def get_user_timeline(
        self,
        screen_name: str = None,
        user_id: int = None,
        since_id: int = None,
        count: int = None,
        max_id: int = None,
        trim_user: bool = None,
        exclude_replies: bool = None,
        include_rts: bool = None,
    ) -> List[TwitterStatusTweet]:
        check_id_or_screen_name(screen_name, user_id)
        return [
            TwitterStatusTweet.from_json(TwitterStatusTweet, v)
            for v in self.full_authenticated_request(
                "GET",
                USER_TIMELINE_PATH,
                params={
                    "user_id": user_id,
                    "screen_name": screen_name,
                    "since_id": since_id,
                    "count": count,
                    "max_id": max_id,
                    "trim_user": trim_user,
                    "exclude_replies": exclude_replies,
                    "include_rts": include_rts,
                },
            )
        ]

    def get_mentions_timeline(
        self,
        count: int = None,
        since_id: int = None,
        max_id: int = None,
        trim_user: bool = None,
        include_entities: bool = None,
    ) -> List[TwitterStatusTweet]:
        return [
            TwitterStatusTweet.from_json(TwitterStatusTweet, v)
            for v in self.full_authenticated_request(
                "GET",
                MENTIONS_TIMELINE_PATH,
                params={
                    "count": count,
                    "since_id": since_id,
                    "max_id": max_id,
                    "trim_user": trim_user,
                    "include_entities": include_entities,
                },
            )
        ]
