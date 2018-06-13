import xlrd
import mysql.connector

def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = mysql.connector.connect(user="root", passwd="123456.", database="itkb", use_unicode=True)
    print('连接上了!')
    return db

def createtable(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 如果存在表Sutdent先删除
    cursor.execute("DROP TABLE IF EXISTS Student")
    sql = """CREATE TABLE Student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )"""

    # 创建Sutdent表
    cursor.execute(sql)

def insertdb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO Student
         VALUES ('001', 'CZQ', 70),
                ('002', 'LHQ', 80),
                ('003', 'MQ', 90),
                ('004', 'WH', 80),
                ('005', 'HP', 70),
                ('006', 'YF', 66),
                ('007', 'TEST', 100)"""

    #sql = "INSERT INTO Student(ID, Name, Grade) \
    #    VALUES ('%s', '%s', '%d')" % \
    #    ('001', 'HP', 60)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print('插入数据失败!')
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

def deletedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM Student WHERE Grade = '%d'" % (100)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       db.commit()
    except:
        print ('删除数据失败!')
        # 发生错误时回滚
        db.rollback()

def updatedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print( '更新数据失败!')
        # 发生错误时回滚
        db.rollback()

def closedb(db):
    db.close()



def main():
    # filename = '信息科技服务台晨报（知识库）-2018.6.12.xls'
    # # 打开excel文件
    # sourcedata = xlrd.open_workbook(filename)
    # # 获取第一张工作表（通过索引的方式）
    # sourcetable = sourcedata.sheets()[0]
    #
    # index = 0
    # while index < sourcetable.nrows:
    #     # data_list用来存放数据
    #     data_list = []
    #     # 将table中第一行的数据读取并添加到data_list中
    #     data_list.extend(sourcetable.row_values(index))
    #     print(data_list)
    #
    #     index += 1

    db = connectdb()    # 连接MySQL数据库

    createtable(db)     # 创建表
    insertdb(db)        # 插入数据
    print('\n插入数据后:')
    querydb(db)
    # deletedb(db)        # 删除数据
    # print ('\n删除数据后:')
    # querydb(db)
    # updatedb(db)        # 更新数据
    # print( '\n更新数据后:')
    # querydb(db)

    closedb(db)         # 关闭数据库

if __name__ == '__main__':
    main()