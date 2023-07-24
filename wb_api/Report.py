import os
from datetime import timedelta, datetime
from mongo.db import DB
from wb_api.APIRequest import *


df_records_map = {"№": "rrd_id",
                          "Номер поставки": "gi_id",
                          "Предмет": "subject_name",
                          "Код номенклатуры": "nm_id",
                          "Бренд": "brand_name",
                          "Артикул поставщика": "sa_name",
                          "Баркод": "barcode",
                          "Тип документа": "doc_type_name",
                          "Обоснование для оплаты": "supplier_oper_name",
                          "Кол-во": "quantity",
                          "Цена розничная": "retail_price",
                          "Вайлдберриз реализовал Товар (Пр)": "retail_amount",
                          "Согласованный продуктовый дисконт, %": "sale_percent",
                          "Итоговая согласованная скидка": "product_discount_for_report",
                          "Цена розничная с учетом согласованной скидки": "retail_price_withdisc_rub",
                          "Размер снижения кВВ из-за акции, %": "is_kgvp_v2",
                          "Скидка постоянного Покупателя (СПП)": "",
                          "Вознаграждение с продаж до вычета услуг поверенного, без НДС": "ppvz_sales_commission",
                          "Возмещение за выдачу и возврат товаров на ПВЗ": "ppvz_reward",
                          "Возмещение издержек по эквайрингу": "acquiring_fee",
                          "Вознаграждение Вайлдберриз (ВВ), без НДС": "ppvz_vw",
                          "НДС с Вознаграждения Вайлдберриз": "ppvz_vw_nds",
                          "К перечислению Продавцу за реализованный Товар": "ppvz_for_pay",
                          "ИНН партнера": "ppvz_inn",
                          "ШК": "shk_id",
                          "Rid": "rid",
                          "Srid": "srid",
                          "Возмещение издержек по перевозке": "rebill_logistic_cost",
                          "Организатор перевозки": "rebill_logistic_org"
                          }


class Reports:
    _uri_path = 'supplier/reportDetailByPeriod'

    @classmethod
    def get_last_week(cls):
        _wb_api = APIRequest()
        _now = datetime.now()
        _param = {
            "dateFrom": _now + timedelta(-_now.weekday(), weeks=-1),
            "dateTo": _now + timedelta(-_now.weekday() - 1)
        }
        try:
            return _wb_api.get_json(cls._uri_path, param=_param)
        except APITechBreak:
            raise ReportException("Технологический перерыв в WB")


class ReportException(Exception):
    pass
