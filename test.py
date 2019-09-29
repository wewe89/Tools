import xlrd
import   pandas  as pd
import numpy
import openpyxl

def search(val):
    # 打开excel文件
    sourcedata = xlrd.open_workbook(r'C:\Users\ZHXY\Desktop\社保局查账\通江.xlsx')
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[1]
    index = 0
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        data_list.extend(sourcetable.row_values(index))
        if(str(data_list[5]).replace('\t','')==val):
            return data_list
        index += 1
    return
def xlrdsearch():
    # 打开excel文件
    sourcedata = xlrd.open_workbook(r'C:\Users\ZHXY\Desktop\社保局查账\通江\通江代发明细.xlsx')
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]
    file = open("db.sql", "w")
    index = 1
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        i = index + 1
        data_list.extend(sourcetable.row_values(index))
        val = data_list[0]
        amount = data_list[1]
        print(type(val),type(amount))
        # data = search(val)
        # line = val + "," + str(amount) + "," + data[2] + "," + data[3] + "," + data[0]
        # line = str(line).replace('\t', '')
        # print(line)
        # file.writelines(line + "\n")
        index += 1
    file.close()
def pdsearch(data,cardno,amount):

    # data = pd.DataFrame(pd.read_excel(r'C:\Users\ZHXY\Desktop\社保局查账\通江\通江 - 副本.xlsx', sheet_name='Sheet2'))
    # print(type(data[u'客户账号'].values[0]), type(data[u'日期'].values[0]), data[u'签约户名'].values[0])
    # print(data[u'客户账号'].values[0], data[u'日期'].values[0], data[u'签约户名'].values[0])
    data = data[(data[u'客户账号'] == cardno) & (data[u'申请金额'] == amount)]
    return data
def searchjigou(data,pich):
    # print(data[u'客户账号'].values[0], data[u'日期'].values[0], data[u'签约户名'].values[0])
    data = data[(data[u'BATCHID'] == pich)]
    if len(data)==0:
        return ''
    else:
        return data[u'COM_ACC_NAME'].values[0]
def pdchaxun():
    pddata = pd.DataFrame(pd.read_excel(r'C:\Users\ZHXY\Desktop\社保局查账\通江\通江.xlsx', sheet_name='Sheet2',
                                      dtype={u'客户账号': numpy.int64, u'申请金额': numpy.float64, u'日期': numpy.int64}))
    picidata = pd.DataFrame(pd.read_excel(r'C:\Users\ZHXY\Desktop\社保局查账\0807_5.xls', sheet_name='1',
                                        dtype={u'BATCHID': numpy.int64}))
    # 打开excel文件
    sourcedata = xlrd.open_workbook(r'C:\Users\ZHXY\Desktop\社保局查账\通江\通江代发明细.xlsx')
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]
    file = open("db.sql", "w")
    index = 1
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        i = index + 1
        data_list.extend(sourcetable.row_values(index))
        cardno = data_list[0]
        amount = data_list[1]
        # date=str(data_list[2]).replace("-","")
        # print(type(cardno), type(date))
        # print(cardno, amount,date)
        data = pdsearch(pddata,numpy.int64(cardno),numpy.float64(amount))
        length = len(data.values)
        line=''
        if (length == 0):
            picihao = ''
            haoma = ''
            huming = ''
            jigou=''
            # geshu = 0
        else:
            for row in data.itertuples():
                # print(getattr(row,u'批次号'))
                picihao = getattr(row,u'批次号')
                haoma = getattr(row,u'证件号码')
                huming = getattr(row,u'签约户名')
                riqi=getattr(row,u'日期')
                jigou=searchjigou(picidata,numpy.int64(picihao))
                line = cardno + "," + str(amount)+ "," + haoma + "," + huming + "," + str(picihao) + "," + str(jigou)+"," + str(riqi)+"," + str(length)
        line = str(line).replace('\t', '')
        print(line)
        file.writelines(line + "\n")
        index += 1
    file.close()
if __name__ == '__main__':
   pdchaxun()
   # df = pd.DataFrame(pd.read_excel(r'C:\Users\ZHXY\Desktop\社保局查账\通江\通江.xlsx', sheet_name='Sheet2'))
   # data = df[u'客户账号']
   # print(type(data.values[0]))
