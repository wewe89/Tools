import requests
import re
import io
import random
import sys
import time
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
        'c0-id':+index,
        'c0-param0':'number:0',
        'c0-param1':'number:10',
        'c0-param2':'null:null',
        'c0-e3':'string:LEDGER',
        'c0-e4':'string:oper_equal',
        'c0-e5':'string:0',
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
        'c1-e21':'string:2',
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
    index=dwrstr.index("s1['CSTM_NO']=")
    str=dwrstr[index+15:index+29]
    return str

if __name__ == '__main__':
    getCSTM_NO(0,'513721199511147236')
