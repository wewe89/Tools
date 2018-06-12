import  xlrd
import xlwt

filename='吴成峦--【new】存款交易明细_对客.xls'
#打开excel文件
sourcedata=xlrd.open_workbook(filename)
#获取第一张工作表（通过索引的方式）
sourcetable=sourcedata.sheets()[0]

destdata=xlwt.Workbook()
desttable=destdata.add_sheet("明细",cell_overwrite_ok=True)
desttable.col(0).width=3000
desttable.col(1).width=3000
desttable.col(2).width=3000
desttable.col(3).width=6000
desttable.col(4).width=6000
desttable.col(5).width=5000

alignment = xlwt.Alignment() # Create Alignment
# May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT,
#HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.horz = xlwt.Alignment.HORZ_CENTER   #水平居中
# May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER    #垂直居中
alignment.wrap=xlwt.Alignment.WRAP_AT_RIGHT

#边框
borders = xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
borders.bottom_colour=0x3A

head_font = xlwt.Font() # 为样式创建字体
head_font.name = '宋体'
head_font.bold=True
head_font.height=0x00DC

head_style = xlwt.XFStyle() # 初始化样式
head_style.font = head_font # 设定样式
head_style.alignment=alignment
head_style.borders=borders

font = xlwt.Font() # 为样式创建字体
font.name = '宋体'
font.height=0x00DC

def_style = xlwt.XFStyle() # 初始化样式
def_style.font = font # 设定样式
def_style.alignment=alignment
def_style.borders=borders

font1 = xlwt.Font() # 为样式创建字体
font1.name = '宋体'
font1.colour_index=2#设置字体颜色
font1.height=0x00DC


red_style = xlwt.XFStyle() # 初始化样式
red_style.font = font1 # 设定样式
red_style.alignment=alignment
red_style.borders=borders

font2 = xlwt.Font() # 为样式创建字体
font2.name = '宋体'
font2.colour_index=3#设置字体颜色
font2.height=0x00DC

green_style = xlwt.XFStyle() # 初始化样式
green_style.font = font2 # 设定样式
green_style.alignment=alignment
green_style.borders=borders

desttable.write(0,0,"交易日期",head_style)
desttable.write(0,1,"金额",head_style)
desttable.write(0,2,"余额",head_style)
desttable.write(0,3,"对方账号",head_style)
desttable.write(0,4,"对方户名",head_style)
desttable.write(0,5,"交易描述",head_style)
index=2
while index<sourcetable.nrows:
    #data_list用来存放数据
    data_list=[]
    #将table中第一行的数据读取并添加到data_list中
    data_list.extend(sourcetable.row_values(index))
    desttable.write(index-1,0,data_list[0],def_style)

    if(data_list[36]=="1"):
        desttable.write(index-1,1,"+"+data_list[10],red_style)
    else:
        desttable.write(index - 1, 1, "-"+data_list[10], green_style)

    desttable.write(index-1,2,data_list[11],def_style)
    desttable.write(index-1,3,data_list[29],def_style)
    desttable.write(index-1,4,data_list[31],def_style)
    desttable.write(index-1,5,data_list[23],def_style)

    index+=1

destdata.save("new"+filename)