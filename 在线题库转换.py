import xlrd
import xlsxwriter

filename='试题批量导入模板.xls'
#打开excel文件
sourcedata=xlrd.open_workbook(filename)
#获取第一张工作表（通过索引的方式）
sourcetable=sourcedata.sheets()[1]

destdata=xlsxwriter.Workbook("new"+filename+"x")
desttable=destdata.add_worksheet("明细")

index=0
while index<sourcetable.nrows:

    #data_list用来存放数据
    data_list=[]
    #将table中第一行的数据读取并添加到data_list中
    data_list.extend(sourcetable.row_values(index))
    str1=','.join(str(i) for i in data_list[0])
    desttable.write(index,0,str1)

    index+=1

destdata.close()