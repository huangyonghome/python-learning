#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 下午7:15
# @Author  : jesse
# @File    : practise.py

import openpyxl

#获取一个execl的workbook对象
wb = openpyxl.load_workbook('example.xlsx')


#查看excel的活跃工作表,也就是打开Excel的sheet
print(wb.active)

#是否已只读模式打开
print(wb.read_only)

#excel字符编码
print(wb.encoding)

#excel中的所有sheet工作表对象
print(wb.worksheets)

#获取所有表格的名称
print(wb.sheetnames)

#获取某个sheet表格的worksheet对象
print(wb['student'])

# print(wb.get_active_sheet())

# print(dir(wb))
#
# for item in dir(wb):
#     if 'active' in item:
#         print(item)
