import os

from dotenv import load_dotenv
from wb_api.Report import Reports
from mongo.db import DB

load_dotenv()

import_dir_path = os.getenv('XLS_PATH_TEMPLATE')

mongo_wb_api_report_collection = "wb_report"


if __name__ == '__main__':
    db = DB()
    report = Reports().get_last_week()
    db.save_to_collection(mongo_wb_api_report_collection, report)

