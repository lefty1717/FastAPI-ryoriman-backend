from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from uvicorn import run

from configuration.core_setting import DOCS_URL, REDOC_URL, OPENAPI_URL, HOST, PORT

from router.test_router import router as TestRouter


def create_application() -> FastAPI:
    application = FastAPI(
        docs_url=DOCS_URL,
        redoc_url=REDOC_URL,
        openapi_url=OPENAPI_URL 
    )

    application.include_router(TestRouter)

    return application

app = create_application()

if __name__ == '__main__':
    run('main:app', host=HOST, port=PORT, reload=True)