import pytest
import asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

from .app import app

client = TestClient(app=app)


@pytest.mark.asyncio
async def test_main():
    async with (AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    )) as client:
        res = await client.get("/main")
        assert res.json() == {"message": "OK"}

@pytest.mark.skip
def test_main_2():
    response = client.get("/main")
    assert response.status_code == 200