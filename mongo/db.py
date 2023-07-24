import os

from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class DB:
    def __init__(self, host: str = None,
                 port: int | str = None,
                 db_name: str = None):
        self.db_host = host or os.getenv('MONGODB_HOST')
        self.db_port = port or os.getenv('MONGODB_PORT')
        self.db = db_name or os.getenv('MONGODB_DB')
        self.db_client = MongoClient(
            f"mongodb://{self.db_host}:{self.db_port}"
        )

    def get_collection(self, collection: str):
        return self.db_client[self.db][collection]

    def save_to_collection(self, coll: str, data):
        self.get_collection(coll).insert_many(data)
