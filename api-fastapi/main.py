from __future__ import annotations
from typing import Optional, Literal

from fastapi import FastAPI, Body, Query

from constants import UserId
from models import ClientViewOfState
from services import BaseBackendService, DummyBackendService


app = FastAPI()
backend: BaseBackendService = DummyBackendService(0)


@app.get("/")
async def get_state(
    user_id: Optional[Literal["new"] | UserId] = Query(None),
) -> ClientViewOfState:
    """
    Get the state of the app.

    If a user ID is "new", a new user will be activated.
    If a valid user ID is given, then the activity of that user will be refreshed.
    If no user ID is provided, then this endpoint will have no side-effects.
    """
    state = backend.get_app_state()

    if user_id is not None:
        if user_id == "new":
            user_id = backend.acquire_user_id()

        backend.activate_user(user_id)

    return ClientViewOfState.from_state(user_id=user_id, state=state)


@app.post("/click")
async def do_click(
    user_id: UserId = Body(),
    number_of_times: int = Body(1),
):
    """
    Click the button. Requires a user ID in the request body.

    Example queries:
    - POST /click << Body: { client_id: 0 }


    Example response:
    - { clicks: 20, users_online: 5 }
    """
    backend.activate_user(user_id)
    backend.increment_clicks(number_of_times)
    state = backend.get_app_state()

    return ClientViewOfState.from_state(state, user_id)


@app.post("/deactivate-user")
async def deactivate_user(user_id: UserId = Body()):
    backend.deactivate_user(user_id)
