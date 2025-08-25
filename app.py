"""
FastAPI application module.

This module defines a FastAPI application with endpoints for basic operations.
It includes lifecycle management, and endpoints for retrieving basic responses.

Endpoints:
    - GET /main: Returns a simple success message.
    - GET /home: Returns a page title for the home page.
"""
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    """
    Async context manager for managing the FastAPI application lifecycle.

    Prints the total runtime of the application when it shuts down.

    Args:
        app: An instance of the FastAPI application.
    """
    start = time.time()
    yield
    print(f"Приложение проработало {time.time()-start}")


app = FastAPI(lifespan=lifespan, debug=False)


@app.get("/main")
async def main() -> JSONResponse:
    """
    Handler for the GET request to the `/main` endpoint.

    Returns:
        JSONResponse: A response with a success message.
    """
    return JSONResponse(status_code=200, content={"message": "OK"})


@app.get("/home")
async def home() -> JSONResponse:
    """
    Handler for the GET request to the `/home` endpoint.

    Returns:
        JSONResponse: A response with the page title.
    """
    return JSONResponse(status_code=200, content={"page_title": "home"})
