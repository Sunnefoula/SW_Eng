from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
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


def get_user_info(user_id: str = "default") -> FullUserProfile:
    profile_infos = {
        "default": {
            "short_description": "my bio",
            "long_bio": "my long  bio"
        },
        "user_1": {
            "short_description": "User_1 bio",
            "long_bio": "user_1 long  bio"
        }
    }

    profile_info = profile_infos[user_id]

    users_content = {
        "default": {
            "name": "sofia",
            "liked_posts": [1] * 9,
            "profile_info": profile_info
        },
        "user_1": {
            "name": "sofia",
            "liked_posts": [],
            "profile_info": profile_info
        }
    }
    user_content = users_content[user_id]
    user = User(**user_content)
    full_user_profile = {
        **profile_info,
        **user.dict()
    }

    print(full_user_profile)
    print(user)

    return FullUserProfile(**full_user_profile)


# specific cases should be put in front of the more general ones , me vs {user_id}
# decorator: use this function in the FastAPI.get() method
@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():
    full_user = get_user_info()

    return full_user


@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_id(user_id: str):
    full_user = get_user_info(user_id)

    return full_user


@app.get("/", response_class=PlainTextResponse)
def home():
    return "Welcome"


