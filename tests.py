"""
Модуль для тестирования FastAPI-приложения.
Содержит асинхронные и синхронные тесты для эндпоинтов.
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
    Асинхронный тест для проверки работы эндпоинта `/main`.

    Использует `AsyncClient` для выполнения асинхронного запроса к FastAPI-приложению.
    Проверяет, что ответ содержит ожидаемое сообщение.

    Returns:
        None: Тест не возвращает значения, но проверяет утверждения.

    Raises:
        AssertionError: Если ответ не соответствует ожидаемому.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        res = await client.get("/main")
        assert res.json() == {"message": "OK"}


@pytest.mark.skip(
    reason="Тест временно отключен. Используется для демонстрации синхронного подхода."
)
def test_main_2() -> None:
    """
    Синхронный тест для проверки работы эндпоинта `/main`.

    Использует `TestClient` для выполнения синхронного запроса к FastAPI-приложению.
    Проверяет, что статус-код ответа равен 200.

    Returns:
        None: Тест не возвращает значения, но проверяет утверждения.

    Raises:
        AssertionError: Если статус-код ответа не равен 200.
    """
    response = client.get("/main")
    assert response.status_code == 200
