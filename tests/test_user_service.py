import pytest
from app.services.user import UserService


@pytest.fixture
def profile_infos():
    val={
        0: {
            "short_description": "my bio",
            "long_bio": "my long  bio"
        }
    }
    return val


@pytest.fixture
def users_content():
    val = {
        0: {
            "liked_posts": [1] * 9,
        }
    }

@pytest.mark.asyncio
async def test_delete_user_works_properly(profile_infos, users_content):
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
    user_service = UserService(profile_infos, users_content)
    user_to_delete = 0
    await user_service.delete_user(user_to_delete)
    assert user_to_delete not in profile_infos
    assert user_to_delete not in users_content

