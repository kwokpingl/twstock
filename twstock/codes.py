# -*- coding: utf-8 -*-
#
# Usage: Load all Taiwan stock code info from csv file
#
# TWSE equities = 上市證券
# TPEx equities = 上櫃證券
#

import csv
import os
from collections import namedtuple


ROW = namedtuple('StockCodeInfo', ['type', 'code', 'name', 'ISIN', 'start',
                                   'market', 'group', 'CFI'])
PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TPEX_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'codes', 'tpex_equities.csv')
TWSE_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'codes', 'twse_equities.csv')

codes = {}


def read_csv(path):
    global codes
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        csvfile.readline()
        for row in reader:
            row = ROW(*row)
            codes[row.code] = row


read_csv(TPEX_EQUITIES_CSV_PATH)
read_csv(TWSE_EQUITIES_CSV_PATH)
