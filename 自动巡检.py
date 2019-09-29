import json
import requests
import sys
import io
from selenium import webdriver
import time
def saveAreaservercheckInfo(cookie):
    url='http://10.128.1.55:808/zoneportal-portlet/AreaDaycheckReport.do?action=saveAreaservercheckInfo'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'Connection': 'keep-alive',
               'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
               'Host': '10.128.1.137:8002',
               'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
               }
    params = {'recordDate': '2019-09-28',
              'frontserverhwisalarm': '2019-09-28',
              'frontservercpu': '2019-09-28',
              'frontservermem': '2019-09-28',
              'frontserverlogfile': '2019-09-28',
              'frontserverlogisok': '2019-09-28',
              'rightserverhwisalarm': '2019-09-28',
              'rightservercpu': '2019-09-28',
              'rightservermem': '2019-09-28',
              'rightserverlogfile': '2019-09-28',
              'rightserverlogisok': '2019-09-28',
              'afterserverhwisalarm': '2019-09-28',
              'afterservercpu': '2019-09-28',
              'aftersevermem': '2019-09-28',
              'afterserverlogfile': '2019-09-28',
              'afterserverlogisok': '2019-09-28',
              'firstCMSCdesk': '2019-09-28',
              'firstCMSDdesk': '2019-09-28',
              'firstCMS': '2019-09-28',
              'firstCMSAgent': '2019-09-28',
              'firstCMSPortNum': '2019-09-28',
              'secondCMSCdesk': '2019-09-28',
              'secondCMSDdesk': '2019-09-28',
              'secondCMS': '2019-09-28',
              'secondCMSAgent': '2019-09-28',
              'secondCMSPortNum': '2019-09-28',
              'firstOCRCdesk': '2019-09-28',
              'firstOCR': '2019-09-28',
              'secondOCRCdesk': '2019-09-28',
              'secondOCRDdesk': '2019-09-28',
              'secondOCR': '2019-09-28',
              'rightsaverhwisalarm': '2019-09-28',
              'aftersaverhwisalarm': '2019-09-28',
              'memoryCheck': '2019-09-28',
              'memory': '2019-09-28',
              'checkresult': '2019-09-28',
              'checkmember': '2019-09-28',
              }
    response=requests.post(url,params, headers=headers,cookies=cookie)
    print(response.text)
    return
def wutouliulanqi(usernamestr,passwordstr):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') #改变标准输出的默认编码

    #建立Phantomjs浏览器对象，括号里是phantomjs.exe在你的电脑上的路径
    browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')

    #登录页面
    url = r'http://10.128.1.55:808/home?p_p_id=58&p_p_lifecycle=0&p_p_state=maximized&p_p_mode=view&saveLastPath=0&_58_struts_action=%2Flogin%2Flogin'

    # 访问登录页面
    browser.get(url)

    # 等待一定时间，让js脚本加载完毕
    browser.implicitly_wait(30)

    #输入用户名
    username = browser.find_element_by_name('username')
    username.send_keys(usernamestr)

    #输入密码
    password = browser.find_element_by_name('_58_password')
    password.send_keys(passwordstr)

    # time.sleep(100)
    #点击“登录”按钮
    login_button = browser.find_element_by_id("loginButton")
    login_button.click()

    browser.implicitly_wait(100)
    # browser.find_element_by_class_name("服务器存储日巡检表").click()
    time.sleep(0.1)
    #网页截图
    # browser.save_screenshot('picture1.png')
    #打印网页源代码
    cookies={}
    for i in browser.get_cookies():
        key=i["name"]
        value=i["value"]
        print(key,"->",value)
        cookies[key] = value
    # browser.implicitly_wait(10000)
    print(cookies)

    # browser.quit()
    return cookies
if __name__ == '__main__':
    username="bazhong"
    password="111111"
    cookie= wutouliulanqi(username,password)
    saveAreaservercheckInfo(cookie)
