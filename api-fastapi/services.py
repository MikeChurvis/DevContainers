from abc import ABC, abstractmethod

from constants import UserId
from models import State


class BaseBackendService(ABC):
    @abstractmethod
    def __init__(self, user_activity_timeout_seconds: int) -> None:
        pass

    @abstractmethod
    def get_app_state(self) -> State:
        pass

    @abstractmethod
    def acquire_user_id(self) -> UserId:
        pass

    @abstractmethod
    def activate_user(self, user_id: UserId):
        pass

    @abstractmethod
    def deactivate_user(self, user_id: UserId):
        pass

    @abstractmethod
    def increment_clicks(self, number_of_times: int):
        pass


class DummyBackendService(BaseBackendService):
    def __init__(self, user_activity_timeout_seconds: int) -> None:
        super().__init__(user_activity_timeout_seconds)
        self.user_activity_timeout_seconds = user_activity_timeout_seconds

        print(
            f"User inactivity timeout set to {user_activity_timeout_seconds} seconds."
        )

    def get_app_state(self) -> State:
        print("Dummy app state retrieved.")
        return State(clicks=0, active_users=[])

    def acquire_user_id(self) -> UserId:
        print("Dummy user ID acquired")
        return 0

    def activate_user(self, user_id: UserId):
        print(f"User with ID {user_id} activated.")

    def deactivate_user(self, user_id: UserId):
        print(f"User with ID {user_id} deactivated.")

    def increment_clicks(self, number_of_times: int):
        print(f"Clicks incremented by {number_of_times}.")
