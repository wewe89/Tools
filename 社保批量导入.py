import requests
import xlrd
import datetime
import base64
import configparser
def query(id):
    payload={
        "dto['aab034id']": "511900",
        "dto['aab034name']": "巴中市",
        "dto['aac002']": id,
        "dto['departmentid']": "511900",
        "dto['departmentname']": "巴中市",
        "dto['aae008']": "402",
        "dto['aae008_desc']": "农村信用联社",
        "dto['aff002']": "C1347951000870",
        "dto['aff002_desc']": "巴中农村商业银行股份有限公司巴州区支行",
        "dto['flag']": "1",
        "gridInfo['grid1_limit']": "10",
        "gridInfo['grid1_start']": "0",
        "gridInfo['grid2_limit']": "10",
        "gridInfo['grid2_start']": "0",
    }
    url="http://9.80.46.79:7001/sccard/yhcard/ka_cardlwzksqcxAction!query.do"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
    res = requests.post(url, data=payload,headers=headers,cookies=getCookies())
    print(res.text)
def getCookies(cookie_str):
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies

def saveinfo(name,id,addr,img,phone,num,file,bankid,bankname,areaid,areaname,cookie_str):
    """男生：1 女生：2"""
    if num % 2 == 0:
        sexid="2"
        sex="女"
    else:
        sexid="1"
        sex="男"
    birthday=id[6:10]+"-"+id[10:12]+"-"+id[12:14]
    # print(id,"-",sex)
    payload = {
        "dto['yh']": "",
        "dto['errorFlag']": "",
        "dto['wd']": "",
        "dto['nodeId']": "",
        "dto['yae200']": "",
        "dto['checkedRadio']": "1",
        "dto['checkedRadioId']": "",
        "dto['aac002_2']": id,
        "theFile": "(binary)",
        "dto['zpway']": "00",
        "dto['rad1']": "1",
        "dto['zpflag']": "",
        "dto['getGA']": "1",
        "dto['aac058']": "01",
        "dto['aac058_desc']": "居民身份证（户口簿）",
        "dto['aac161']": "CHN",
        "dto['aac161_desc']": "中国 China",
        "dto['aac1478']": "",
        "dto['aac147']": id,
        "dto['aab099']": "20990101",
        "dto['aac002']": id,
        "dto['aac003']": name,
        "dto['aac004']": sexid,
        "dto['aac004_desc']": sex,
        "dto['aac005']": "01",
        "dto['aac005_desc']": "汉族",
        "dto['aac006']": birthday,
        "dto['aae007']": "636000",
        "dto['aca111']": "",
        "dto['aac067']": phone,
        "dto['aae005']": "",
        "dto['aac200']": "511900",
        "dto['aac200_desc']": "巴中市",
        "dto['sc']": "",
        "dto['targetDepartId']": areaid,
        "dto['targetDepart']": areaname,
        "dto['aab034']": "",
        "dto['aab034_desc']": "",
        "dto['aae008']": "402",
        "dto['aae008_desc']": "农村信用联社",
        "dto['aff002']": bankid,
        "dto['aff002_desc']": bankname,
        "dto['aae006']": addr,
        "dto['aac010']": "",
        "dto['aac042']": "",
        "dto['aac043']": "",
        "dto['aac043_desc']": "",
        "dto['aac044']": "",
        "dto['aac202']": "",
        "dto['aac204']": "0",
        "dto['aac204_desc']": "待发卡",
        "dto['aac060']": "1",
        "dto['aac060_desc']": "正常",
        "dto['aab001']": "",
        "dto['aab004']": "",
        "dto['msg']": "",
        "dto['show']": "",
        "dto['urlGA']": "",
        "dto['yae735_treeId']": areaid,
        "dto['yae735_treeName']": areaname,
        "dto['strbase64']": img,
        "dto['strbase64lt']": "",
        "dto['wdwd']": bankid,
        "dto['flag']": "1",
        "dto['base64_z']": "",
        "dto['base64_f']": "",
    }
    url = "http://9.80.46.79:7001/sccard/yhcard/ka_cardlwlxzkAction!save.do"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept - Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'9.80.46.79:7001',
        'Origin':'http://9.80.46.79:7001',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type': 'multipart/form-data',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'Referer': 'http://9.80.46.79:7001/sccard/yhcard/ka_cardlwlxzkAction!importZip333.do'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
    res = requests.post(url, data=payload, headers=headers,cookies=getCookies(cookie_str))
    # print(res.text)
    str=""
    try:
        jsontext=res.json()
        str=name+"--"+id+"--"+addr+"--"+phone+"--"+"导入失败"+"---"+jsontext["msgBox"]["msg"]
    except:
        str=name+"--"+id+"--"+addr+"--"+phone+"--"+"导入成功"
    print(str)
    file.writelines(str+"\n")
import json
import time
def getage(number):
    current = int(time.strftime("%Y"))
    year = int(number[6:10])
    return current - year

def batchHandleXLS(filename,sheet):

    photo_man=base64.b64encode(open('files/社保待录信息/男.png','rb').read())
    photo_woman = base64.b64encode(open('files/社保待录信息/女.png', 'rb').read())
    img=""

    # 打开excel文件
    sourcedata = xlrd.open_workbook(filename+".xls")
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[sheet]
    index = 0
    f = open(filename+str(sheet)+'.txt', 'w')

    test_cfg = "./社保批量配置文件.cfg"
    config_raw = configparser.RawConfigParser()
    config_raw.read(test_cfg, "utf-8")
    bankid = config_raw.get('Section1', 'bankid')
    bankname = config_raw.get('Section1', 'bankname')
    areaid = config_raw.get('Section1', 'areaid')
    areaname = config_raw.get('Section1', 'areaname')
    cookie_str = config_raw.get('Section1', 'cookie_str')

    while index < sourcetable.nrows:
        # data_list用来存放数据
        lineinfo = []
        # 将table中第一行的数据读取并添加到data_list中
        lineinfo.extend(sourcetable.row_values(index))
        username = lineinfo[0].replace(" ", "")  # 用户名
        id = lineinfo[1].replace(" ","").replace("x","X")  # 身份证号码
        addr = lineinfo[2].replace(" ", "") # 地址
        # addr = "巴中市巴州区光辉乡" # 地址
        if username!="" and id!="" and len(id)==18:
            age=0
            sex=0
            try:
                phone = str(lineinfo[3])[0:11]  # 电话号码
            except:
                phone=""
            try:
                current = int(time.strftime("%Y"))
                year = int(id[6:10])
                age= current - year
                sex = int(id[16:17])
            except :
                print("------------------------")
                index = index + 1
                continue
            if phone=="" or len(phone)!=11:
                phone="13800000000"
            if(age>=0 and age<=60):
                if sex % 2 == 0:
                    img = photo_woman
                else:
                    img=photo_man
                saveinfo(username,id,addr,img,phone,sex,f,bankid,bankname,areaid,areaname,cookie_str)
                # print(index+1,"-",username,"-",id,"-",phone,"-",addr,"-",int(id[16:17]))
        index = index + 1
    f.close()

def loadConfig():
    test_cfg = "./社保批量配置文件.cfg"
    config_raw = configparser.RawConfigParser()
    config_raw.read(test_cfg,"utf-8")
    bankid = config_raw.get('Section1', 'bankid')
    bankname = config_raw.get('Section1', 'bankname')
    areaid = config_raw.get('Section1', 'areaid')
    areaname = config_raw.get('Section1', 'areaname')
    cookie_str = config_raw.get('Section1', 'cookie_str')
    # print(bankid,bankname,areaname,cookie_str)
if __name__ == '__main__':
    # loadConfig()
    test_cfg = "./社保批量配置文件.cfg"
    config_raw = configparser.RawConfigParser()
    config_raw.read(test_cfg, "utf-8")
    filename = config_raw.get('Section1', '文件名')
    # print(filename)
    batchHandleXLS('files/社保待录信息/'+filename,0)
