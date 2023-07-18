from os import environ, getenv

from pymongo import MongoClient

from configuration.core_setting import config

connect = MongoClient(config('DB_STR', default=environ.get('DB_STR', '')))

def get_database():
    return connect['db']
