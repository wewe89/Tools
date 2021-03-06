import requests
import sys
import io
import json
import xlrd

def postDwr(index,id):
    headers = {
        'content-type': 'text/plain',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
    }

    url = "http://10.128.1.124:8001/scom/dwr/call/plaincall/Multiple.2.dwr"
    params = {
        'callCount':'2',
        'page':'/scom/screen/errordispose/dealnoteselect/ledgerlistQuery.jsp?modleid\':\'tradeselect',
        'httpSessionId':'y80hbhlXLwcQCRgYnGcdwK8PTQGFF4QTpQNf227KqqVcKytdCp9h!1947543175',
        'scriptSessionId':'19EAFF47B7D0D244219E7E2BB2EF8D54128',
        'c0-scriptName':'ledgerListQuery',
        'c0-methodName':'obtainDataList',
        'c0-id':'0',
        'c0-param0':'number:0',
        'c0-param1':'number:10',
        'c0-param2':'null:null',
        'c0-e3':'string:LEDGER',
        'c0-e4':'string:oper_equal',
        'c0-e5':'string:'+str(index),
        'c0-e6':'string:',
        'c0-e2':'Object_Condition:{fieldName:reference:c0-e3, oper:reference:c0-e4, value1:reference:c0-e5, value2:reference:c0-e6}',
        'c0-e8':'string:VALUE',
        'c0-e9':'string:oper_equal',
        'c0-e10':'string:'+str(id),
        'c0-e11':'string:',
        'c0-e7':'Object_Condition:{fieldName:reference:c0-e8, oper:reference:c0-e9, value1:reference:c0-e10, value2:reference:c0-e11}',
        'c0-e13':'string:MODLEID',
        'c0-e14':'string:oper_equal',
        'c0-e15':'string:tradeselect',
        'c0-e16':'string:',
        'c0-e12':'Object_Condition:{fieldName:reference:c0-e13, oper:reference:c0-e14, value1:reference:c0-e15, value2:reference:c0-e16}',
        'c0-e1':'Array:[reference:c0-e2,reference:c0-e7,reference:c0-e12]',
        'c0-param3':'Object_And:{conditions:reference:c0-e1}',
        'c0-param4':'null:null',
        'c1-scriptName':'ledgerListQuery',
        'c1-methodName':'getRowCount',
        'c1-id':'1',
        'c1-e19':'string:LEDGER',
        'c1-e20':'string:oper_equal',
        'c1-e21':'string:'+str(index),
        'c1-e22':'string:',
        'c1-e18':'Object_Condition:{fieldName:reference:c1-e19, oper:reference:c1-e20, value1:reference:c1-e21, value2:reference:c1-e22}',
        'c1-e24':'string:VALUE',
        'c1-e25':'string:oper_equal',
        'c1-e26':'string:'+str(id),
        'c1-e27':'string:',
        'c1-e23':'Object_Condition:{fieldName:reference:c1-e24, oper:reference:c1-e25, value1:reference:c1-e26, value2:reference:c1-e27}',
        'c1-e29':'string:MODLEID',
        'c1-e30':'string:oper_equal',
        'c1-e31':'string:tradeselect',
        'c1-e32':'string:',
        'c1-e28':'Object_Condition:{fieldName:reference:c1-e29, oper:reference:c1-e30, value1:reference:c1-e31, value2:reference:c1-e32}',
        'c1-e17':'Array:[reference:c1-e18,reference:c1-e23,reference:c1-e28]',
        'c1-param0':'Object_And:{conditions:reference:c1-e17}',
        'c1-param1':'null:null',
        'batchId':'7',
    }
    resp = requests.post(url, params, headers=headers, cookies=getScomCookies())
    persioninfo = resp.content.decode('unicode-escape')
    return persioninfo
def getCSTM_NO(index,id):
    #0身份证号码     1客户号    2卡号
    dwrstr=postDwr(index,id)
    index=dwrstr.find("s1['CSTM_NO']=")
    if(index==-1):
        return -1
    str=dwrstr[index+15:index+29]
    return str


#获取用户信息
def downloadFile(userid,Acct_Num,username,index,startDate,endDate):
    url='http://10.128.1.137:8002/rsp/fastrpt/exp.do'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    params = {'exportListId': '8a00804e57230095015741c8bd721097',
              'exportPageSize': '50',
              'exportPageNo': '1',
              'exportPageType': '1',
              'exportType': 'xls',
              'fileName': '',
              'remake': '',
              'paras': '{rptId=8a00804e57230095015741bbde701078, isExtemporeQuery=true, favoriteName=%E3%80%90new%E3%80%91%E5%AD%98%E6%AC%BE%E4%BA%A4%E6%98%93%E6%98%8E%E7%BB%86_%E5%AF%B9%E5%AE%A2, isQuery=true}',
              'p_cust_no': userid,
              'p_cust_no_RTRN_SQL_INFO': '##null',
              'p_tx_date1': startDate,
              'p_tx_date2': endDate,
              'p_in_acct_no': Acct_Num,
              'p_in_acct_no_RTRN_SQL_INFO': '##null',
              'Impt_Med_ID': '',
              'Impt_Med_ID_RTRN_SQL_INFO': 'null##null',
              'p_card_no': '',
              'p_card_no_RTRN_SQL_INFO': '##null',
              }
    response=requests.post(url,params, headers=headers, cookies=getSCBICookie())
    open("files/客户明细下载/"+str(index)+username+"【new】存款交易明细_对客.xls","wb").write(response.content)
    return
#内部账户
def getPersonAcct_Num(username,userId,cardNo,startDate,endDate):
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.137:8002/rsp/fastrpt/dataGrid.do?listId=8a00804e57230095015741c8bd721097&isExtempore=false'
    # 查询个人信息
    params = {  'exportListId': '8a00804e57230095015741c8bd721097',
                'exportPageSize': '',
                'exportPageNo': '',
                'exportPageType': '',
                'exportType': '',
                'fileName': '',
                'remake': '',
                'paras': '{rptId=8a00804e57230095015741bbde701078, isExtemporeQuery=true, favoriteName=%E3%80%90new%E3%80%91%E5%AD%98%E6%AC%BE%E4%BA%A4%E6%98%93%E6%98%8E%E7%BB%86_%E5%AF%B9%E5%AE%A2, isQuery=true}',
                'p_cust_no': userId,
                'p_cust_no_RTRN_SQL_INFO': '##null',
                'p_tx_date1': startDate,
                'p_tx_date2': endDate,
                'p_in_acct_no': '',
                'p_in_acct_no_RTRN_SQL_INFO': '##null',
                'Impt_Med_ID': cardNo,
                'Impt_Med_ID_RTRN_SQL_INFO': 'null##null',
                'p_card_no': '',
                'p_card_no_RTRN_SQL_INFO': '##null',
                'page': '1',
                'rows': '50',
                }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=getSCBICookie())
    persioninfo = resp.content.decode('utf-8')
    #print(persioninfo)
    info=json.loads(persioninfo)
    rows=info['rows']
    index=0
    while(index<len(rows)):
        if(rows[index]["Acct_Num"]!=""):
            # print(rows[index]["Acct_Num"])
            return rows[index]["Acct_Num"]
        else:
            print(username)
        index=index+1
    return
#获取用户信息
def getTotalNum(username,userId,accountNum,index,startDate,endDate):
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.137:8002/rsp/fastrpt/dataGrid.do?listId=8a00804e57230095015741c8bd721097&isExtempore=false'
    # 查询个人信息
    params = {  'exportListId': '8a00804e57230095015741c8bd721097',
                'exportPageSize': '',
                'exportPageNo': '',
                'exportPageType': '',
                'exportType': '',
                'fileName': '',
                'remake': '',
                'paras': '{rptId=8a00804e57230095015741bbde701078, isExtemporeQuery=true, favoriteName=%E3%80%90new%E3%80%91%E5%AD%98%E6%AC%BE%E4%BA%A4%E6%98%93%E6%98%8E%E7%BB%86_%E5%AF%B9%E5%AE%A2, isQuery=true}',
                'p_cust_no': userId,
                'p_cust_no_RTRN_SQL_INFO': '##null',
                'p_tx_date1': startDate,
                'p_tx_date2': endDate,
                'p_in_acct_no': accountNum,
                'p_in_acct_no_RTRN_SQL_INFO': '##null',
                'Impt_Med_ID': '',
                'Impt_Med_ID_RTRN_SQL_INFO': 'null##null',
                'p_card_no': '',
                'p_card_no_RTRN_SQL_INFO': '##null',
                'page': '1',
                'rows': '50',
                }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=getSCBICookie())
    persioninfo = resp.content.decode('utf-8')
    info=json.loads(persioninfo)
    # print(info)
    return info["total"]
def getScomCookies():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = r'JSESSIONID=PYXycdSW103QP8ZLJFRvbkDn8LhyqQZPHT4h81J07Bg8fHlgvwB3!-1534195959'
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies
def getSCBICookie():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str =\
        'imoiaRspTopMenuType=small; imoiaRspLoginName=760504; imoiaRspLoginType=run; BIGipServerscbi_report_8002_pool=3456139274.16927.0000; ADMINCONSOLESESSION=Gakdxh9XtucDBH8VUHZGGDDWR9MbsUJlY4iaOOXOWkrFKaDeSc!330034839'
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies
def batchHandleCSV():
    file = open("明细表.csv", "r")  # 打开文件
    startDate = '2002-01-01'
    endDate = '2019-07-02'

    for index, line in enumerate(file.readlines()):
        userid=""#客户号
        #id = ""  # 身份证号码
        cardNo = ""  # 卡号
        username = ""  # 用户名
        Acct_Num="" #内部账号
        line = line.replace(" ", "")
        lineinfo = line.strip().split(",")
        #id = lineinfo[2]  # 身份证号码
        # cardNo = lineinfo[1]  # 卡号
        username = lineinfo[0]  # 用户名
        userid=lineinfo[1]
        if userid=="":
            # 0身份证号码     1客户号    2卡号
            userid = getCSTM_NO(2, cardNo)
            if (userid == -1):
                print(index + 1, username, "未找到记录")
                continue
        # Acct_Num = getPersonAcct_Num(username, userid, cardNo, startDate, endDate)  # 内部账户
        getTotalNum(username, userid, Acct_Num, index + 1, startDate, endDate)
        downloadFile(userid, Acct_Num, username, index + 1, startDate, endDate)
    file.close()  # 关闭文件

def batchHandleXLS():

    startDate = '2018-01-01'
    endDate = '2019-07-23'

    filename = 'files/客户明细下载/查日均客户信息表.xlsx'
    # 打开excel文件
    sourcedata = xlrd.open_workbook(filename)
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]
    index=0
    while index<sourcetable.nrows:
        # data_list用来存放数据
        lineinfo = []
        # 将table中第一行的数据读取并添加到data_list中
        lineinfo.extend(sourcetable.row_values(index))
        id = lineinfo[2].replace(" ","")  # 身份证号码
        cardNo = lineinfo[1].replace(" ","")  # 卡号
        # cardNo = "" # 卡号  查所有
        username = lineinfo[0].replace(" ","")  # 用户名
        # 0身份证号码     1客户号    2卡号
        userid=lineinfo[3].replace(" ","")#客户号
        if(userid==""):
            userid = getCSTM_NO(0, id)
        print(index+1,username,id,cardNo, end=' ')
        if (userid == -1):
            print("未找到记录", end=' ')
        else:
            if cardNo=="":
                Acct_Num=""
            else:
                Acct_Num = getPersonAcct_Num(username, userid, cardNo, startDate, endDate)  # 内部账户
            if Acct_Num==None:
                Acct_Num=""
            totalnum=getTotalNum(username, userid, Acct_Num, index + 1, startDate, endDate)
            print(userid,Acct_Num,totalnum, end=' ')
            downloadFile(userid, Acct_Num, username, index + 1, startDate, endDate)

        index=index+1
        print()

if __name__ == '__main__':
    batchHandleXLS()
