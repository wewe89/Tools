import xlrd
import mysql.connector
import re
import string
import time
def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '123456',
        'port': 3306,
        'database': 'shebao',
        'charset': 'utf8'
    }
    db = mysql.connector.connect(**config)
    print('连接上了!')
    return db

def insertShebaodb(db,id_i,mer_seq_id, id, name,pay_amount, create_time,canal_type):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    param = (id_i,mer_seq_id,id,name,pay_amount,create_time,canal_type)
    # SQL 插入语句
    sql = 'INSERT INTO shebaoshoufei(id_i,mer_seq_id,id,name,pay_amount,create_time,canal_type) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    #sql = "INSERT INTO Student(ID, Name, Grade) \
    #    VALUES ('%s', '%s', '%d')" % \
    #    ('001', 'HP', 60)
    try:
        # 执行sql语句
        cursor.execute(sql,param)
        # 提交到数据库执行
        db.commit()
    except mysql.connector.Error as e:
        # Rollback in case there is any error
        print('query error!{}'.format(e),id_i)
        db.rollback()

def closedb(db):
    db.close()

def handleShebaoFile(filename):
    db = connectdb()    # 连接MySQL数据库
    # 打开excel文件
    sourcedata = xlrd.open_workbook(filename)
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]

    index = 0
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        data_list.extend(sourcetable.row_values(index))
        # # print(data_list)
        # timeArray = time.strptime(tss2, "%Y-%m-%d %H:%M:%S")
        # # 转为其它显示格式
        # otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
        # otherStyleTime  # 2013/10/10 23:40:00
        insertShebaodb(db, index+1,data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6])  # 插入数据

        index += 1

    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    handleShebaoFile("files/社保局明细/新建 XLS 工作表 (2)(3).xls")