import requests
import sys
import os
import re
import json
import xlrd
def get_all(cwd):
    result = []
    get_dir = os.listdir(cwd)
    for i in get_dir:
        sub_dir = os.path.join(cwd,i)
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            result.append(i)
    return result
def cal_avg(filename):

    # 打开excel文件
    sourcedata = xlrd.open_workbook(filename)
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]
    index = 2
    totalamount = 0
    while index < sourcetable.nrows:
        # data_list用来存放数据
        lineinfo = []
        # 将table中第一行的数据读取并添加到data_list中
        lineinfo.extend(sourcetable.row_values(index))
        amount = lineinfo[11].replace(" ", "")
        totalamount = totalamount + float(amount)
        index = index + 1
    avg = totalamount / (sourcetable.nrows - 2)
    return '%.2f'%avg
import openpyxl
if __name__ == '__main__':
    dir=r'files/客户明细下载'
    res=get_all(dir)
    f = open('files/日均存款结果.txt', 'w')

    workbook = openpyxl.load_workbook("files\查日均客户信息表.xlsx")
    worksheet = workbook.worksheets[0]
    for filename in res:
        st = re.findall(r"\d+\.?\d*", filename)
        index = int(st[0])
        worksheet["E"+st[0]]=cal_avg(dir+"/"+filename)
        strs=st[0]+"---"+cal_avg(dir+"/"+filename)
        f.writelines(strs+"\n")
        print(strs)
    workbook.save("files\查日均客户信息表.xlsx")
