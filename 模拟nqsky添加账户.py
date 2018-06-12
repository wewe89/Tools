import requests
import sys
import io
import json
#获取用户信息
def getPersioninfo(userId):
    # 登录后才能访问的网页
    url = 'http://10.128.1.79/mdm/user/deviceUser/query/queryUserList.do?t=3'
    # 查询个人信息
    params = {'groupId': '306', 'hasDevice': '是否有设备', 'otherInfo': userId, 'needActive': 'true', 'isRoot': 'true',
              'currentPage': '1', 'pageSize': '15', 'totalPage': '1'}
    # 在发送get请求时带上请求头和cookies
    resp = requests.post(url, params, headers=headers, cookies=cookies)
    persioninfo = resp.content.decode('utf-8')
    info=json.loads(persioninfo)
    if(len(info['data'])==0):
        return





    return info['data'][0]

# 插入数据 loginId柜员号 userId系统id
def insertUserInfo(type,loginId,userId):
    url = 'http://10.128.1.79/mdm/device/edit/deviceRegist.do'
    # userId=getUserid(loginId)
    # if (userId is None):
    #     print("未找到该用户")
    #     return
    #ios
    iosparams = {
    'deviceOSType':'2',
    'deviceType':'20',
    'relationship':'2',
    'deviceNumber':'',
    'deviceName':loginId+'-IOS-001',
    'serialNum':'',
    'imei':'',
    'wifiMac':'',
    'versioNum':'',
    'loginIdOfDevice':loginId,
    'userIdOfDevice':userId,
    'action':'add',
    'status':'1',
    'id':'',
    }
    #android
    androidparams = {
        'deviceOSType': '1',
        'deviceType': '10',
        'relationship': '2',
        'deviceNumber': '',
        'deviceName': loginId+'-Android-001',
        'serialNum': '',
        'imei': '',
        'wifiMac': '',
        'versioNum': '',
        'loginIdOfDevice': loginId,
        'userIdOfDevice': userId,
        'action': 'add',
        'status': '1',
        'id': '',
    }
    if(type=="安卓系统"):
        print("android--------")
        params=androidparams
    else:
        print("ios--------")
        params=iosparams
    resp = requests.post(url,params, headers=headers, cookies=cookies)
    insterinfo=resp.content.decode('utf-8')
    print(insterinfo)
    return


def getUserid(loginId):
    # file = open("所有.txt", "r",encoding='UTF-8')  # 打开文件
    # for index, line in enumerate(file.readlines()):
    #     lineinfo = line.strip().split(",")
    #     if(lineinfo[0]==loginId):
    #         file.close()
    #         return lineinfo[3]
    # file.close()
    userid=getPersioninfo(loginId)['id']
    return

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
# 浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'__guid=127623693.1887088056366755600.1523323164480.7434; JSESSIONID=RM15hNYS2XM0N0kdrPcxhQt6n6ckBbhDJTbDHVTsSGMmKkJYJfnN!1777104735; monitor_count=19'
# 把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
# 设置请求头
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}



file = open("test.csv", "r")  # 打开文件
for index, line in enumerate(file.readlines()):
    lineinfo=line.strip().split(",")
    persioninfo = getPersioninfo(lineinfo[2])
    if(persioninfo is None):
        print(lineinfo[0] + "--"+lineinfo[1] + "--" + lineinfo[2] + "--" + '未查询到该柜员号!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        continue
    # print(persioninfo)
    if( persioninfo['registNum'] == 0 and persioninfo['activeNum'] == 0 ):
        print(lineinfo[0] + "--"+lineinfo[1]+"--"+lineinfo[2]+"--"+'需要注册')
        insertUserInfo(lineinfo[3],lineinfo[2],persioninfo['id'])
    else:
        print(lineinfo[0] + "--"+lineinfo[1]+"--"+lineinfo[2]+"--"+'已经注册')

file.close()  # 关闭文件

