from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()  # instance of FastAPI


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The Username",
        description="whatever...",
        min_length=1,
        default=None
    )
    liked_posts: List[int] = Field(
        description="Array of ids the user liked",
    )


class FullUserProfile(User):
    short_description: str
    long_bio: str


class MultipleUserResponse(BaseModel):
    users: List[FullUserProfile]
    total: int


class CreateUserResponse(BaseModel):
    user_id: int


profile_infos = {
    0: {
        "short_description": "my bio",
        "long_bio": "my long  bio"
    }
}
users_content = {
    0: {
        "liked_posts": [1] * 9,
    }
}


async def get_user_info(user_id: int = 0) -> FullUserProfile:

    # currently reading from dictonary
    profile_info = profile_infos[user_id]
    user_content = users_content[user_id]
    # later reading from DB: wait

    user = User(**user_content)
    full_user_profile = {
        **profile_info,
        **user.dict()
    }

    return FullUserProfile(**full_user_profile)


async def get_all_users_with_pagination(start: int, limit: int) -> (List[FullUserProfile],int):
    list_of_users = []
    keys = list(profile_infos.keys())
    total = len(keys)
    for index in range(0, len(keys), 1):
        if index < start:
            continue
        current_key = keys[index]
        user = await get_user_info(current_key)
        list_of_users.append(user)
        if len(list_of_users) >= limit:
            break

    return list_of_users, total


async def create_update_user(full_profile_info: object, user_id: object = None) -> object:
    """
    Create user and if not exist updates the user
    :param full_profile_info: FullUserProfile - user info save in database
    :param user_id:
    :return: use_id: int
    """
    if user_id is None:
        user_id = len(profile_infos)  # entries in the dictionary
    liked_posts = full_profile_info.liked_posts
    short_description = full_profile_info.short_description
    long_bio = full_profile_info.long_bio

# update the dictionaries:
    users_content[user_id] = {"liked_posts": liked_posts}
    profile_infos[user_id] = {
        "short_description": short_description,
        "long_bio": long_bio}

    print("users_content:", users_content)
    print("profile_infos:", profile_infos)
    return user_id


async def delete_user(user_id: int) -> None:
    del profile_infos[user_id]
    del users_content[user_id]


# specific cases should be put in front of the more general ones , me vs {user_id}
# decorator: use this function in the FastAPI.get() method
@app.get("/user/me", response_model=FullUserProfile)
async def test_endpoint():
    full_user = await get_user_info()

    return full_user


@app.get("/user/{user_id}", response_model=FullUserProfile)
async def get_user_id(user_id: int):
    """
    Endpoint for retrieving a FullUserProfile by user's id
    :param user_id: int
    :return: FullUserProfile
    """
    full_user = await get_user_info(user_id)
    # without await keyword in an async fnct, fnct is not executed, just a reference to it

    return full_user


@app.put("/user/{user_id}")
async def update_user(user_id: int, full_profile_info: FullUserProfile):
    await create_update_user(full_profile_info, user_id)
    return None


@app.delete("/user/{user_id}")
async def remove_user(user_id: int):
    await delete_user(user_id)


@app.get("/Users", response_model=MultipleUserResponse)
async def get_all_users_paginated(start: int = 0, limit: int = 2):
    users, total = await get_all_users_with_pagination(start=start, limit=limit)
    formatted_users = MultipleUserResponse(users=users, total=total)
    return formatted_users


#sending data to server
@app.post("/User", response_model=CreateUserResponse)
async def add_user(full_profile_info: FullUserProfile):
    user_id = await create_update_user(full_profile_info)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user

