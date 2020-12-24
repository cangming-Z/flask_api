# encoding:utf-8

import xlrd
import xlwt


# 读取xls文件
def read_xls(path, sheet_name):
    # 获取xls文件对象
    book = xlrd.open_workbook(path)
    # 根据sheet名称获取具体sheet
    sheet = book.sheet_by_name(sheet_name)
    return sheet


# 写入xls文件
# path：包含完整文件名的路径
def write_xls(path, sheet_name):
    work_book = xlwt.Workbook()
    sheet_1 = work_book.add_sheet(sheet_name, cell_overwrite_ok=True)
    sheet_1.write("")
    work_book.save(path)
