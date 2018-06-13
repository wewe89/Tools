import requests
import sys
import io
import json
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
    response=requests.post(url,params, headers=headers, cookies=cookies)
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
    resp = requests.post(url, params, headers=headers, cookies=cookies)
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
    resp = requests.post(url, params, headers=headers, cookies=cookies)
    persioninfo = resp.content.decode('utf-8')
    info=json.loads(persioninfo)
    print(str(index)+"----"+username+"------"+str(info["total"]))
    return

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
# 浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = 'imoiaRspTopMenuType=big; imoiaRspLoginType=exp; __guid=165233471.4210132586760320500.1526280137524.9197; ADMINCONSOLESESSION=oBfxhUF5CJcU63cttx_H_bu9WY4JMtyO9kgozeeWBSPoW_0Fgq!21315747; BIGipServerscbi_report_8002_pool=3472916490.16927.0000'
# 把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
# 设置请求头
# userid="76590001352915"
# cardNo="6214571781004506692"
# username=''
# Acct_Num = getPersonAcct_Num(userid,cardNo)
# downloadFile(userid,Acct_Num)

file = open("监察委查询名单.csv", "r")  # 打开文件
startDate='2002-01-01'
endDate='2018-06-12'

for index, line in enumerate(file.readlines()):
    lineinfo=line.strip().split(",")
    userid = lineinfo[3]
    cardNo = lineinfo[2]
    username = lineinfo[1]
    Acct_Num = getPersonAcct_Num(username,userid,cardNo,startDate,endDate)
    getTotalNum(username,userid,Acct_Num,lineinfo[0],startDate,endDate)
    downloadFile(userid,Acct_Num,username,lineinfo[0],startDate,endDate)

file.close()  # 关闭文件

