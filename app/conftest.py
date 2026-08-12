import hashlib
from datetime import datetime

import pytest_asyncio
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.utilities.db import db


async def add_db_test_user() -> None:
    """
    Add test user to Database
    """
    await db.tokens.update_one(
        {"user": "tester"},
        {
            "$set": {
                "access_token_hash": hashlib.sha256(
                    "GOOD_TOKEN".encode()
                ).hexdigest(),
                "created_date": datetime.utcnow(),
            }
        },
        upsert=True,
    )


@pytest_asyncio.fixture(autouse=True)
async def seed_test_user() -> None:
    """
    Ensure the test user/token exists in the DB before every test
    """
    await add_db_test_user()


@pytest_asyncio.fixture()
async def test_client() -> AsyncClient:
    """
    Create an instance of the client
    """
    return AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
        follow_redirects=True,
    )
