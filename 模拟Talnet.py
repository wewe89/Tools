# -*- coding: utf-8 -*-

import telnetlib
import os

def talnet():
    '''Telnet远程登录：Windows客户端连接Linux服务器'''

    # 配置选项
    Host = '192.168.1.2'  # Telnet服务器IP
    username = 'admin'  # 登录用户名
    password = '123456'  # 登录密码
    finish = ':~$ '  # 命令提示符（标识着上一条命令已执行完毕）

    # 连接Telnet服务器
    tn = telnetlib.Telnet(Host)

    # 输入登录用户名
    tn.read_until('login: ')
    tn.write(username + '\n')

    # 输入登录密码
    tn.read_until('Password: ')
    tn.write(password + '\n')

    # 登录完毕后，执行ls命令
    tn.read_until(finish)
    tn.write('ls\n')

    # ls命令执行完毕后，终止Telnet连接（或输入exit退出）
    tn.read_until(finish)
    tn.close()  # tn.write('exit\n')
def cmd():
    list = ["taobao", "jd", "baidu", "126", "dinpay", ""]  # 需要扫描的域名名称
    i = 0
    strlist = []  # 组装最后完整的网站域名
    while list[i] != list[-1]:  # 不是列表list最后一个元素空格时，则进入
        str = "ping -c 5 www."  # 在linux系统中ping网站的域名的语法
        strlist.append(str + list[i] + ".com")  # 组装成完整的域名
        os.system(strlist[i])  # 调用os模块进行ping操作
        i = i + 1
if __name__ == '__main__':
    cmd()