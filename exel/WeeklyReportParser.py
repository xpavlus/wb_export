import logging
import os
from glob import glob
from os.path import isfile

import pandas


def parse_xls(xls_file):
    """
    Convert exel-file to DataFrame dict
    :param xls_file: path to exel
    :return: {<sheet>: DataFrame}
    """
    xl = pandas.ExcelFile(xls_file)
    df_result = {}
    for sheet in xl.sheet_names:
        df_result[sheet] = xl.parse(sheet)
    return df_result


class WeeklyReportParserException(Exception):
    pass


class WeeklyReportParser:
    df_record_exel_map = {"№": "rrd_id",
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

    def __init__(self, path):
        imports = glob(path)
        for f in imports:
            if isfile(f):
                xls_data = parse_xls(f)
                if "Sheet1" in xls_data.keys():
                    self._df = xls_data["Sheet1"]
                    logging.info(f"File: {f} has been imported")
                else:
                    raise WeeklyReportParserException("Wrong structure of the exel-file, there is no Sheet1 page")
                os.unlink(f)
            else:
                raise WeeklyReportParserException(f"File ({f}) does not exist")
