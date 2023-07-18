import os
from os import environ
from starlette.config import Config

PROFILE: str = environ.get('PROFILE', 'local')
config = Config(f'.env.{PROFILE}')

#project config
CONTEXT_PATH: str = '/ryoriman-api'
API_PREFIX: str = f'{CONTEXT_PATH}'
PROJECT_NAME: str = 'ryoriman'

SCHEMA: str = config('SCHEMA', default=environ.get('SCHEMA', 'http'))
HOST: str = config('HOST', default=environ.get('HOST', ''))
PORT: int = config('PORT', cast=int ,default=8888)
ORIGIN: str = f'{SCHEMA}://{HOST}:{PORT}'

# fastapi setting
DOCS_URL = f'{CONTEXT_PATH}/docs'
REDOC_URL = f'{CONTEXT_PATH}/rdoc'
OPENAPI_URL = f'{CONTEXT_PATH}/openapi.json'