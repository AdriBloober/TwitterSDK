from typing import List

from twitter.models import TwitterModel


class IDCursorList(TwitterModel):
    ids: List[int]
    next_cursor: int
    next_cursor_str: str
    previous_cursor: int
    previous_cursor_str: str