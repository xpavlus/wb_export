import random
from unittest import TestCase
from random import choices
from string import ascii_letters, digits
from pymongo import MongoClient
from os import getenv
from mongo.db import DB
from dotenv import load_dotenv

load_dotenv()


def str_gen(num: int = 8) -> str:
    _simbols = ascii_letters
    _simbols += digits
    return ''.join(choices(_simbols, k=num))


class TestDB(TestCase):
    _db_name = 'testdb_' + str_gen()
    _db_collection_name = 'test_' + str_gen()
    _db_client = MongoClient(f"mongodb://{getenv('MONGODB_HOST')}:{getenv('MONGODB_PORT')}")
    _db_row = "row_" + str_gen()
    _db_value = "data_" + str_gen(random.randrange(6, 100))
    _db_store_data = {_db_row: _db_value}

    def setUp(self):
        self._db = self._db_client[self._db_name]
        self._db_collection = self._db[self._db_collection_name]
        self._db_collection.insert_one(self._db_store_data)

    def tearDown(self) -> None:
        self._db_client.drop_database(self._db_name)

    def test_get_collection(self):
        db = DB(
            host=getenv('MONGODB_HOST'),
            port=getenv('MONGODB_PORT'),
            db_name=self._db_name
        )
        collection = db.get_collection(self._db_collection_name)
        _res = collection.find_one(self._db_store_data)
        self.assertTrue(self._db_row in _res)
