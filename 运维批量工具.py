import requests
import json


def getCookies():
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码
    # 浏览器登录后得到的cookie，也就是刚才复制的字符串
    # 把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    return cookies
def xiugai(batchid,end_stat,work_stat):
    payload={"batchid":batchid,"end_stat":end_stat,"work_stat":work_stat}
    url="http://10.128.1.149:7001/bsms//bat/batinfoadm_edit?requesttype=ajax"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
    res = requests.post(url, data=json.dumps(payload),headers=headers,cookies=getCookies())
    print(res.text)
def chaxun(work_date,end_stat):
    payload={"prd_code":"0827000008","work_date":work_date,"end_stat":end_stat,"start":1,"limit":100}
    url="http://10.128.1.149:7001/bsms//bat/batinfoadm_query?requesttype=ajax"
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
    res = requests.post(url, data=json.dumps(payload),headers=headers,cookies=getCookies())
    return json.loads(res.text)
cookie_str = r'__guid=199844526.2354567148642618400.1563154117183.0176; JSESSIONID=M5tunqTSio41T7efnBHi9aDyvLSUgNdyxvL_4tgChYt65DVkAIuI!1919125977; monitor_count=35'
def 批量修改状态(date):
    # "20190729"
    jsontext=chaxun(date,"F")
    listtext=json.loads(jsontext["actionresult"])['field1']
    for item in listtext:
        # i=json.loads(item)
        # xiugai(item["batchid"])
        print(item["batchid"]+"----"+item["dealmsg"])
import datetime

import calendar
def 批量查询():
    start = '20190801'
    end = '20190802'

    datestart = datetime.datetime.strptime(start, '%Y%m%d')
    dateend = datetime.datetime.strptime(end, '%Y%m%d')

    while datestart < dateend:
        date=datestart.strftime('%Y%m%d')
        # print(date)
        jsontext=chaxun(date,"F")
        listtext = json.loads(jsontext["actionresult"])['field1']
        for item in listtext:
            # i=json.loads(item)
            print(date+"----"+item["batchid"]+"----"+item["dealmsg"])

        datestart += datetime.timedelta(days=1)

if __name__ == '__main__':
    批量查询()