"""
Module for testing the FastAPI application.
Contains asynchronous and synchronous tests for API endpoints.
"""

import pytest
import asyncio
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

from .app import app

client = TestClient(app=app)


@pytest.mark.asyncio
async def test_main() -> None:
    """
    Asynchronous test for the `/main` endpoint.

    Uses `AsyncClient` to perform an asynchronous request to the FastAPI application.
    Verifies that the response contains the expected message.

    Returns:
        None: The test does not return a value but checks assertions.

    Raises:
        AssertionError: If the response does not match the expected result.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        res = await client.get("/main")
        assert res.json() == {"message": "OK"}


@pytest.mark.skip(
    reason="Test temporarily disabled. Used for synchronous approach demonstration."
)
def test_main_2() -> None:
    """
    Synchronous test for the `/main` endpoint.

    Uses `TestClient` to perform a synchronous request to the FastAPI application.
    Verifies that the response status code is 200.

    Returns:
        None: The test does not return a value but checks assertions.

    Raises:
        AssertionError: If the response status code is not 200.
    """
    response = client.get("/main")
    assert response.status_code == 200
