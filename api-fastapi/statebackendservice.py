from abc import ABC, abstractmethod
from typing import Optional

from .types import UserId, FrameId, FrameInfo


class BaseBackendService(ABC):
    @abstractmethod
    def __init__(self, user_inactivity_timeout_sec: int) -> None:
        """
        user_inactivity_timeout_ms: the duration in seconds that a user will remain active after their last activity.
        """
        pass

    @abstractmethod
    def initialize_frame(
        frame_id: Optional[FrameId], *, clicks: int = 0, active_users: list[UserId] = []
    ) -> FrameInfo:
        pass

    @abstractmethod
    def has_frame(frame_id: FrameId) -> bool:
        pass

    @abstractmethod
    def destroy_frame(frame_id: FrameId) -> bool:
        pass

    @abstractmethod
    def activate_user(
        frame_id: FrameId, user_id: Optional[UserId]
    ) -> tuple[UserId, FrameInfo]:
        pass

    @abstractmethod
    def is_user_active(frame_id: FrameId, user_id: UserId) -> bool:
        pass

    @abstractmethod
    def deactivate_user(frame_id: FrameId, user_id: UserId) -> FrameInfo:
        pass

    @abstractmethod
    def increment_clicks(frame_id: FrameId, by_amount: int) -> FrameInfo:
        pass
