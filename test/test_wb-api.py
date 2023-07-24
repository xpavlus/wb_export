import datetime
import json
from unittest import TestCase
from wb_api.APIRequest import APIRequest


class TestAPIRequest(TestCase):
    wb_url = "statistics-api-sandbox.wildberries.ru"
    wb_path = "supplier/reportDetailByPeriod"
    dateFrom = datetime.datetime.now() - datetime.timedelta(days=7)
    dateTo = datetime.datetime.now()
    parm = {
        "dateFrom": dateFrom.strftime('%Y-%m-%d'),
        "dateTo": dateTo.strftime('%Y-%m-%d')
    }
    api = APIRequest(domain=wb_url)

    def test_get(self):
        with self.assertRaises(ValueError):
            self.api.get_json(1, self.parm)
        rq = self.api._get(self.wb_path, self.parm)
        self.assertTrue(rq.ok)

    def test_get_json(self):
        _rq = self.api.get_json(self.wb_path, self.parm)
        self.assertIsInstance(_rq, list)
        self.assertTrue(len(_rq) > 1)

