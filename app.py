import time

from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.responses import JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    start = time.time()
    yield
    print(f"Приложение проработало {time.time()-start}")


app = FastAPI(lifespan=lifespan, debug=False)


@app.get("/main")
async def main():
    return JSONResponse(status_code=200, content={"message": "OK"})
