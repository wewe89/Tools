import requests
import sys
import io
import json
import xlrd
import re
def dataGrid(userId):
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.137:8002/rsp/user/dataGrid.do'
    # 查询个人信息
    params = {  'loginName':userId,
                'userName':'',
                'userType':'',
                'page':'1',
                'rows':'10',
                'sort':'loginName',
                'order':'asc',
                }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=getSCBICookie())
    persioninfo = resp.content.decode('utf-8')
    print(persioninfo)
    info=json.loads(persioninfo)
    return info["rows"][0]

def save(user):
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.137:8002/rsp/user/save.do'
    # 查询个人信息
    params = {  'userId':user["userId"],
                'branchChg':'0',
                'loginPassword':'aBcDe',
                'branchNo':user["branchNo"],
                'branchNoA':user["branchNo"],
                'branchNoB':'',
                'branchNoC':'',
                'branchNoD':'',
                'branchNoE':'',
                'loginName':user["userId"],
                'userName':user["userName"],
                'userType':user["userType"],
                'userStatus':'1',
                'branchName':user["branchNm"],
                'branchNameA':user["branchNm"],
                'branchNameB':'',
                'branchNameC':'',
                'branchNameD':'',
                'branchNameE':'',
                'userTel':user["userTel"],
                'userMobTel':user["userMobTel"],
                }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=getSCBICookie())
    persioninfo = resp.content.decode('utf-8')
    print(persioninfo)
    return
def userRunRoleSave(userid):
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.137:8002/rsp/user/userRunRoleSave.do'
    # 查询个人信息
    params = {  'userId':userid,
                'ids':'2c90a55b432cb8fc01432cc26aa90008,8a00804e54f073d2015500febc6c0568,8a00804f4fd5ea68014fd8fdcf7f0025'
                }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=getSCBICookie())
    persioninfo = resp.content.decode('utf-8')
    print(persioninfo)
    return
# 添加系统资源
def addResource(userid):
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.20:8001/SCMDM/jsp/commonInvokeAction.do'
    # 查询个人信息
    params = {
               'funcname': 'XtzzhBP.add',
               'intryid': '2010181830',
               'intxtzyid': '141',
                'nextpage': '%2FSCMDM%2Fjsp%2Fryjggl%2Fxtzzhlst.jsp%3Fintryid%3D2010181830%26strzh%'+userid+'%26strryxm%3D%B3%C2%C5%F4',
                'strxtzh': userid,
                'trans': '1'
                }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=getOACookie())
    persioninfo = resp.content.decode('GBK')
    pat = r'''alert\((.*?)\);'''
    s=re.search(pat,persioninfo).group()
    print(s)
    return
# 添加系统资源
def delResource(userid):
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.20:8001/SCMDM/jsp/commonInvokeAction.do'
    # 查询个人信息
    params = {
               'funcname': 'XtzzhBP.del',
               'intxtzyid': '141',
                'nextpage': '%2FSCMDM%2Fjsp%2Fryjggl%2Fxtzzhlst.jsp%3Fintryid%3D2010181830%26strzh%'+userid+'%26strryxm%3D%B3%C2%C5%F4',
                'strxtzh': userid,
                'trans': '1'
                }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=getOACookie())
    persioninfo = resp.content.decode('GBK')
    pat = r'''alert\((.*?)\);'''
    s=re.search(pat,persioninfo).group()
    print(s)
    return
def getSCBICookie():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = 'imoiaRspTopMenuType=big; imoiaRspLoginType=run; __guid=165233471.4210132586760320500.1526280137524.9197; ADMINCONSOLESESSION=j9QhItlpVe85xhwbU_2-z3ja7ID2Rz2l4LbzN60dooXpGHzqFg!2023316238; BIGipServerscbi_report_8002_pool=3456139274.16927.0000'
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies
def getOACookie():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    cookies["BIGipServerscmdm_pool"] = '453017610.16671.0000'
    cookies["SCMDM_JSESSIONID"] = 'H1TqbHJNLCs08MQmr1myrWJkgFQHvSHMDNgndYyW8F1vRYjtJLB0!1399423705'
    return cookies
def getBranchName(branchID):
    file = open("files/获取机构名称", "r")  # 打开文件

    jsonstr=file.read()
    jsonstr=jsonstr.replace("\\n","")
    new_dict=json.loads(jsonstr)
    for val in new_dict:
        # print(val)
        if(val["branchNo"]==str(branchID)):
            return val["text"]

    file.close()  # 关闭文件
def searchByUserNo(userid):
    # headers = {'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, application/x-ms-xbap, */*',
    #            'Accept-Encoding': 'gzip, deflate',
    #            'Accept-Language': 'zh-CN',
    #            'Connection': 'Keep-Alive',
    #
    #            # 'Content - Length': '121',
    #            'Content-Type': 'application/x-www-form-urlencoded',
    #            'Cookie': 'BIGipServerscmdm_pool=453017610.16671.0000; SCMDM_JSESSIONID=82fkbHKbT75spkZwyBG8JpJh5FD3XCmgj9dJbtLnpzcpj123J9hc!1399423705',
    #            'Host': '10.128.1.20:8001',
    #            'Referer': 'http://10.128.1.20:8001/SCMDM/jsp/ryjggl/tree/jgygtreeshow.jsp?key=strnbjgbz=1@stryxxzbz=2@intjgyglx=0@strjgccbm=00010015@intcxtjlx=0@strhzjgxsbz=0',
    #            'User-agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3)',
    #            }
    headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Cookie': 'BIGipServerscmdm_pool=453017610.16671.0000; SCMDM_JSESSIONID=bdmGbHfpyQGjWQpJ1bHfktlX0L2sR4fnrjdCQK5n6lRy011L9g40!1399423705',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.20:8001',
               'Referer': 'http://10.128.1.20:8001/SCMDM/jsp/ryjggl/tree/jgygtreeshow.jsp?key=strnbjgbz=1@stryxxzbz=2@intjgyglx=0@strjgccbm=00010015@intcxtjlx=0@strhzjgxsbz=0',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    # 登录后才能访问的网页
    url = 'http://10.128.1.20:8001/SCMDM/jsp/ryjggl/tree/jgyglist.jsp'
    # 查询个人信息
    params = {
       'key': 'strnbjgbz%3D1@intjgyglx%3D0@stryxxzbz%3D2@strjgccbm%3D00010015@intcxtjlx%3D0@strhzjgxsbz%3D0',
       'strcxlx': '3',
        'strdwmc': userid,
    }
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers)
    persioninfo = resp.content.decode('GBK')
    pat = r'''<div class="dtxs">(.*?)>'''
    print(persioninfo)
    s = re.findall(pat, persioninfo)
    print(s)
    return
def batchHandleXLS():
    filename = 'files/申请事项（巴州区支行）.xlsx'
    # 打开excel文件
    sourcedata = xlrd.open_workbook(filename)
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]
    index=3
    while index<sourcetable.nrows:
        # data_list用来存放数据
        lineinfo = []
        # 将table中第一行的数据读取并添加到data_list中
        lineinfo.extend(sourcetable.row_values(index))

        userid=str(lineinfo[2])[0:6]

        #SCBI操作
        # userinfo = dataGrid(userid)
        # save(userinfo)
        # userRunRoleSave(userid)

        #添加系统资源
        delResource(userid)

        index=index+1

if __name__ == '__main__':
    # branchName=getBranchName(7618)
    # print(branchName)
    # userid=770216
    # userinfo=dataGrid(userid)
    # save(userinfo)
    # userRunRoleSave(userid)

    # batchHandleXLS()
    # addResource('764705')
    searchByUserNo('760504')