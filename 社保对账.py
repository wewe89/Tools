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

def insertdb(db,id,details_id,order_id,mer_seq_id,order_type,order_amount,pay_amount,mer_no,mer_name,fund_channel,ori_mer_seq_id,ori_details_id,refund_amount,order_status,pay_status_update_time,pay_status,create_time,update_time):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    param = (id,details_id,order_id,mer_seq_id,order_type,order_amount,pay_amount,mer_no,mer_name,fund_channel,ori_mer_seq_id,ori_details_id,refund_amount,order_status,pay_status_update_time,pay_status,create_time,update_time)
    # SQL 插入语句
    sql = 'INSERT INTO weixinshoufei(id,details_id,order_id,mer_seq_id,order_type,order_amount,pay_amount,mer_no,mer_name,fund_channel,ori_mer_seq_id,ori_details_id,refund_amount,order_status,pay_status_update_time,pay_status,create_time,update_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
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

def querydb(db,mer_seq_id):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT create_time FROM weixinshoufei where pay_status='02' and mer_seq_id='"+mer_seq_id+"'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            # print(row[0])
            return row[0]
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

    index = 0
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        data_list.extend(sourcetable.row_values(index))
        # print(data_list)
        insertdb(db, index+1,data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5], data_list[6], data_list[7],data_list[8], data_list[9], data_list[10], data_list[11],data_list[12], data_list[13], data_list[14],data_list[15], data_list[16])  # 插入数据

        index += 1
    sourcetable = sourcedata.sheets()[1]

    index = 0
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        data_list.extend(sourcetable.row_values(index))
        # print(data_list)
        insertdb(db, index + 1, data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5],
                 data_list[6], data_list[7], data_list[8], data_list[9], data_list[10], data_list[11], data_list[12],
                 data_list[13], data_list[14], data_list[15], data_list[16])  # 插入数据

        index += 1

    closedb(db)         # 关闭数据库

def verify(filename):
    db = connectdb()    # 连接MySQL数据库
    # 打开excel文件
    sourcedata = xlrd.open_workbook(filename)
    # 获取第一张工作表（通过索引的方式）
    sourcetable = sourcedata.sheets()[0]

    f = open('files/社保局明细/微信对账结果.csv', 'w')

    index = 0
    while index < sourcetable.nrows:
        # data_list用来存放数据
        data_list = []
        # 将table中第一行的数据读取并添加到data_list中
        data_list.extend(sourcetable.row_values(index))
        # print(data_list)
        row=querydb(db,data_list[1])
        oneline=data_list[0]+","+data_list[1]+","+data_list[2]+","+data_list[3]+","+str(data_list[4])+","+data_list[5]+","+data_list[6]+","+data_list[7]+","
        if row:
            oneline=oneline+"存在,"+str(row)
        else:
            oneline=oneline+"不存在"
        f.writelines(oneline+"\n")
        index += 1
    f.close()
    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    # handleFile("files/社保局明细/副本巴中人社导订单数据.xls")

    verify("files/社保局明细/自助缴费查询.xlsx")