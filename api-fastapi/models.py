from __future__ import annotations
from typing import Optional

from pydantic import BaseModel

from constants import UserId


class State(BaseModel):
    clicks: int
    active_users: list[UserId]


class ClientViewOfState(BaseModel):

    """
    Serialized as
    {
        "user_id": (typeof UserId) | null,
        "clicks": int,
        "users_online": int
    }
    """

    user_id: Optional[UserId]
    clicks: int
    users_online: int

    @classmethod
    def from_state(cls, state: State, user_id: Optional[UserId]):
        return cls(
            user_id=user_id, clicks=state.clicks, users_online=len(state.active_users)
        )
