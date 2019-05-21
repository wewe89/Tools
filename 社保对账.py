import xlrd
import mysql.connector
import re
import string
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

def insertdb(db,yijiname,erjiname,dingdanhao,riqi,shijian,leixing,qudao,zhangtai,jine):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    param = (yijiname,erjiname,dingdanhao,riqi,shijian,leixing,qudao,zhangtai,jine)
    # SQL 插入语句
    sql = 'INSERT INTO weixinshoufei(yijiname,erjiname,dingdanhao,riqi,shijian,leixing,qudao,zhuangtai,jine) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
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
        print('query error!{}'.format(e))
        db.rollback()

def querydb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT * FROM Student"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ID = row[0]
            Name = row[1]
            Grade = row[2]
            # 打印结果
            print("ID: %s, Name: %s, Grade: %d" % \
                (ID, Name, Grade))
    except:
        print ("Error: unable to fecth data")


def closedb(db):
    db.close()

def handleFile(filename):
    db = connectdb()    # 连接MySQL数据库
    # 打开excel文件
    sourcedata = xlrd.open_workbook(filename)
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]

    index = 1
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        data_list.extend(sourcetable.row_values(index))
        print(data_list)
        insertdb(db, data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6], data_list[7],data_list[8])  # 插入数据

        index += 1

    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    handleFile("files/社保局明细/巴中社保/社保网上收单明细201811.xlsx")
    handleFile("files/社保局明细/巴中社保/社保网上收单明细201812.xlsx")
    handleFile("files/社保局明细/巴中社保/社保网上收单明细201901.xlsx")
    handleFile("files/社保局明细/巴中社保/社保网上收单明细201902.xlsx")