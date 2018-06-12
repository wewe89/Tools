import xlrd
import xlsxwriter

filename='【new】内部账交易明细.xls'
#打开excel文件
sourcedata=xlrd.open_workbook(filename)
#获取第一张工作表（通过索引的方式）
sourcetable=sourcedata.sheets()[0]

destdata=xlsxwriter.Workbook("new"+filename)
desttable=destdata.add_worksheet("明细")

headStyle = destdata.add_format({
    'font_name':'黑体',
    'font_size':10,                 #字体大小
    'bold':True,                   #是否粗体
    # 'bg_color':'#101010',              #表格背景颜色
    # 'font_color':'#FEFEFE',             #字体颜色
    'align':'center',                #居中对齐
    'valign':'vcenter',                #居中对齐
    'top':1,                     #上边框 #后面参数是线条宽度
    'left':1,                    #左边框
    'right':1,                    #右边框
    'bottom':1                    #底边框
})
def_style = destdata.add_format({
    'font_name':'宋体',
     'font_size':10,                 #字体大小
    #  'bold':True,                   #是否粗体
    'text_wrap':True,                   #自动换行
    # 'bg_color':'#101010',              #表格背景颜色
    # 'font_color':'#FEFEFE',             #字体颜色
    'align':'center',                #居中对齐
    'valign':'vcenter',                #居中对齐
    'top':1,                     #上边框 #后面参数是线条宽度
    'left':1,                    #左边框
    'right':1,                    #右边框
    'bottom':1                    #底边框
})
red_style = destdata.add_format({
    'font_name':'宋体',
    'font_size':10,                 #字体大小
    # 'bold':True,                   #是否粗体
    # 'bg_color':'#101010',              #表格背景颜色
     'font_color':'#ff6600',             #字体颜色
    'align':'center',                #居中对齐
    'valign':'vcenter',                #居中对齐
    'top':1,                     #上边框 #后面参数是线条宽度
    'left':1,                    #左边框
    'right':1,                    #右边框
    'bottom':1                    #底边框
})
green_style = destdata.add_format({
    'font_name':'宋体',
    'font_size':10,                 #字体大小
    # 'bold':True,                   #是否粗体
    # 'bg_color':'#101010',              #表格背景颜色
    'font_color':'#339933',             #字体颜色
    'align':'center',                #居中对齐
    'valign':'vcenter',                #居中对齐
    'top':1,                     #上边框 #后面参数是线条宽度
    'left':1,                    #左边框
    'right':1,                    #右边框
    'bottom':1                    #底边框
})
desttable.set_column("A:A",10)
desttable.set_column("B:B",20)
desttable.set_column("C:C",8)
desttable.set_column("D:D",8)
desttable.set_column("E:E",20)
desttable.set_column("F:F",15)
desttable.set_column("G:G",30)
desttable.set_row(0,22)

desttable.write(0,0,"会计日期",headStyle)
desttable.write(0,1,"交易时间",headStyle)
desttable.write(0,2,"交易金额",headStyle)
desttable.write(0,3,"余额",headStyle)
desttable.write(0,4,"对方账号",headStyle)
#desttable.write(0,5,"对方户名",headStyle)
desttable.write(0,5,"交易描述",headStyle)

index=2
while index<sourcetable.nrows:

    desttable.set_row(index-1, 22)
    #data_list用来存放数据
    data_list=[]
    #将table中第一行的数据读取并添加到data_list中
    data_list.extend(sourcetable.row_values(index))
    desttable.write(index-1,0,data_list[23],def_style)
    desttable.write(index-1,1,data_list[5],def_style)

    if(data_list[10]=="1"):
        desttable.write(index-1,2,"+"+str(data_list[9]),red_style)
    else:
        desttable.write(index-1,2,"-"+str(data_list[9]),green_style)

    desttable.write(index-1,3,data_list[17],def_style)
    desttable.write(index-1,4,data_list[14],def_style)
    #desttable.write(index-1,5,'',def_style)
    desttable.write(index-1,5,data_list[26],def_style)

    index+=1

destdata.close()