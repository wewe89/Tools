import requests
import re
import io
import random
import sys
import time
def getCookies():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = r'__guid=199830062.2154591976785360000.1526609124348.26; JSESSIONID=vQWpbFRVp9PxZPpjSdVNfN9yxk6Zv6Vm1sXGptSDTmNj64kjbjv8!-404869194'
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies
def getCustomInfo(pageIndex,pageSize):
    headers = {
        'content-type': 'text/plain',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
    }

    url = "http://10.128.1.124:8001/scom/dwr/call/plaincall/Multiple.2.dwr"
    params = {
        'callCount':'2',
        'page':'/scom/screen/maintenancedata/paramadjust/instclerk/clerkstandarddata.jsp?modleid=clerkstandarddata',
        'httpSessionId':'kgcKb1nLTDyy523pR1Jff1cpY8RYF9MdtvDX9Kd1QDHLtsh56K4Z!-404869194',
        'scriptSessionId':'0A44A66D17B64514DDA26529282331A5393',
        'c0-scriptName':'ClerkStandDataProvider',
        'c0-methodName':'obtainDataList',
        'c0-id':'0',
        'c0-param0':'number:'+str(pageIndex),
        'c0-param1':'number:'+str(pageSize),
        'c0-param2':'null:null',
        'c0-e1':'string:MODLEID',
        'c0-e2':'string:oper_equal',
        'c0-e3':'string:clerkstandarddata',
        'c0-e4':'string:',
        'c0-param3':'Object_Condition:{fieldName:reference:c0-e1, oper:reference:c0-e2, value1:reference:c0-e3, value2:reference:c0-e4}',
        'c0-param4':'null:null',
        'c1-scriptName':'ClerkStandDataProvider',
        'c1-methodName':'getRowCount',
        'c1-id':'1',
        'c1-e5':'string:MODLEID',
        'c1-e6':'string:oper_equal',
        'c1-e7':'string:clerkstandarddata',
        'c1-e8':'string:',
        'c1-param0':'Object_Condition:{fieldName:reference:c1-e5, oper:reference:c1-e6, value1:reference:c1-e7, value2:reference:c1-e8}',
        'c1-param1':'null:null',
        'batchId':'2',
    }
    resp = requests.post(url, params, headers=headers, cookies=getCookies())
    persioninfo = resp.content.decode('unicode-escape')
    # print(persioninfo)
    return persioninfo
def parseInfo(info):
    val = {}
    i = 1
    while (i != 0):
        pat = r's' + str(i) + r'''\['(.*?)'\]="(.*?)"'''
        customlist = re.findall(pat, info)
        if (len(customlist) == 0):
            i = 0
            break
        list = {}
        for l in customlist:
            list[l[0]] = l[1]
        val[i - 1] = list
        i = i + 1
        # print(customlist)
    return val
def handleCustomInfo(value):
    for index in value:
        if((int(value[index]['INST_NO'])>=7571) & (int(value[index]['INST_NO'])<=7703)):
            if((int(value[index]['INST_NO'])!=7702)&(int(value[index]['INST_NO'])!=7575)):
                if(value[index]['TLR_LVL']=='4'):
                    print(value[index]['TLR_NAME'],"-----",value[index]['TLR_NO'],'-----------',value[index]['INST_NO'])

if __name__ == '__main__':
    length=1
    pageIndex=1
    while length!=0:
        print("-------------------------------------------------------第",pageIndex,"页---------------------------------------------------------------")
        info=getCustomInfo((pageIndex-1)*10,10)
        value=parseInfo(info)
        handleCustomInfo(value)

        pageIndex=pageIndex+1
        length=len(value)
