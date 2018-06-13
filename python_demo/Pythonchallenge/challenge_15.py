#!usr/bin/python
# -*- coding:utf-8 -*-
from calendar import isleap
from datetime import date

TUESDAY = 1

# 从1800年到2000年
for year in range(1000, 2000):
    t = date(year, 1, 27)
    # 是闰年并且1月的27号是星期一
    if isleap(year) and t.weekday() == TUESDAY:
        print(t.isoformat())
