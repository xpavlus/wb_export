import os

from dotenv import load_dotenv
from wb_api.Report import *
from mongo.db import *

load_dotenv()

import_dir_path = os.getenv('XLS_PATH_TEMPLATE')

mongo_wb_api_report_collection = "wb_report"


if __name__ == '__main__':
    db = DB()
    try:
        report = Reports().get_last_week()
    except ReportException as e:
        raise Exception(e)
    db.save_to_collection(mongo_wb_api_report_collection, report)

