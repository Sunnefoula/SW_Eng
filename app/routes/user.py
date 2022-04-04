from fastapi import APIRouter,HTTPException, Response, Depends
from app.schemas.user import (
    CreateUserResponse,
    FullUserProfile,
    MultipleUserResponse,
)
from app.services.user import UserService
from app.dependecies import rate_limit
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(levelname)-6s %(name)-10s %(asctime)-8s %(message)s",
    datefmt="%y-%m-%d", # year month day Hour Minute Sec
    filename="log.txt")
logger.setLevel(logging.INFO)  # debug -> inf0 -> warn -> error -> critical
print(__name__)  # app.routes.user
# different log levels:
#logger.debug()
#logger.info()
#logger.warning()
#logger.error()
#logger.critical()
console = logging.StreamHandler()
full_logger = logging.getLogger('')
full_logger.addHandler(console)


def create_user_router(profile_infos: dict, users_content: dict) -> APIRouter:
    user_router = APIRouter(
        prefix="/user",
        tags=["user"],
        dependencies=[Depends(rate_limit)]
    )
    user_service = UserService(profile_infos, users_content)

    @user_router.get("/all", response_model=MultipleUserResponse)
    async def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_all_users_with_pagination(start=start, limit=limit)
        formatted_users = MultipleUserResponse(users=users, total=total)
        return formatted_users

    @user_router.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_id(user_id: int):
        """
        Endpoint for retrieving a FullUserProfile by user's id
        :param response:
        :param user_id: int
        :return: FullUserProfile
        """
        #try:
        full_user = await user_service.get_user_info(user_id)
        # without await keyword in an async fnct, fnct is not executed, just a reference to it
        #except KeyError:
        #    logger.error(f"Invalid user_id {user_id}")
         #   raise HTTPException(status_code=404, detail=f"User with id {user_id} doesnt exist")

        return full_user

    @user_router.put("/{user_id}")
    async def update_user(user_id: int, full_profile_info: FullUserProfile):
        await user_service.create_update_user(full_profile_info, user_id)
        return None

    @user_router.delete("/{user_id}")
    async def remove_user(user_id: int):
        logger.info(f"about to delete userid")
        #try:
        await user_service.delete_user(user_id)
        #except KeyError:
        #    raise HTTPException(status_code=404, detail="User doesnt exist")

    # sending data to server
    @user_router.post("/", response_model=CreateUserResponse)
    async def add_user(full_profile_info: FullUserProfile):
        user_id = await user_service.create_update_user(full_profile_info)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    return user_router

