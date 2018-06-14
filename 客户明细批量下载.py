import requests
import sys
import io
import json

def getCookies():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = r'__guid=199830062.2154591976785360000.1526609124348.26; JSESSIONID=45zLbvTfs2f87FLVTGGPbXj42LKcQlrSF1vmrBB9jrKpX9QT5GpH!1947543175'
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies
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
        'c0-e10':'string:'+id,
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
        'c1-e26':'string:'+id,
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
    resp = requests.post(url, params, headers=headers, cookies=getCookies())
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
    open("监察委查询名单/"+str(index)+username+"【new】存款交易明细_对客.xls","wb").write(response.content)
    return
#获取用户信息
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
    # print(persioninfo)
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
    print(str(index)+"----"+username+"------"+str(info["total"])+"------"+accountNum)
    return

def getSCBICookie():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = 'imoiaRspTopMenuType=big; imoiaRspLoginType=exp; __guid=165233471.4210132586760320500.1526280137524.9197; BIGipServerscbi_report_8002_pool=3456139274.17183.0000; ADMINCONSOLESESSION=xsH9KSMH9Y4cfuXbJINTYEkxRV-lQ7iAiBBgIa7FaHibVJb3WS!-1965563594'
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies
def batchHandle():
    file = open("明细表.csv", "r")  # 打开文件
    startDate = '2002-01-01'
    endDate = '2018-06-14'

    for index, line in enumerate(file.readlines()):
        # if((index+1) in [24,35,63,66,67,110,137,]):
        #     continue
        line = line.replace(" ", "")
        lineinfo = line.strip().split(",")
        id = lineinfo[2]  # 身份证号码
        cardNo = lineinfo[1]  # 卡号
        username = lineinfo[0]  # 用户名
        userid = getCSTM_NO(0, id)
        if (userid == -1):
            print(index + 1, username, "未找到记录")
            continue
        # Acct_Num = getPersonAcct_Num(username, userid, cardNo, startDate, endDate)  # 内部账户
        # getTotalNum(username, userid, Acct_Num, index + 1, startDate, endDate)
        # downloadFile(userid, Acct_Num, username, index + 1, startDate, endDate)
    file.close()  # 关闭文件
if __name__ == '__main__':
    batchHandle()
