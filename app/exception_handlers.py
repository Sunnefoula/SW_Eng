from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exception import UserNotFound
import logging


logger = logging.getLogger(__name__)


def add_exception_handler(app: FastAPI) -> None: # accept an application of type FastAPI
    @app.exception_handler(UserNotFound)
    async def handle_user_not_found(request: Request, exc: UserNotFound):
        logger.error(f"Non existent user_id :{exc.user_id} was requested")
        return JSONResponse(status_code=404, content=f"User with id {exc.user_id} doesnt exist")
