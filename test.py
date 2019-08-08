import xlrd
import   pandas  as pd
# 打开excel文件
sourcedata = xlrd.open_workbook(r'C:\Users\ZHXY\Desktop\社保局查账\恩阳代发失败清单.xlsx')
res=pd.DataFrame(pd.read_excl(r'C:\Users\ZHXY\Desktop\社保局查账\恩阳.xlsx',sheetname="Sheet2"))
# 获取第一张工作表（通过索引的方式）
sourcetable = sourcedata.sheets()[1]
file=open("db.sql","w")
index = 0
while index < sourcetable.nrows:
    # data_list用来存放数据
    data_list = []
    # 将table中第一行的数据读取并添加到data_list中
    i=index+1
    data_list.extend(sourcetable.row_values(index))
    print(data_list)
    # file.writelines("INSERT INTO AFA_BATCH_TASK_DTL (PRD_CODE, SUB_PRD_CODE, BATCH_TYPE, BATCH_DESC, CITY_CODE, COUNTY_CODE, HEAD_ACC, COM_ACC, COM_ACC_NAME, INST_NO, EFFECT_FLAG, RESERVE1, RESERVE2, RESERVE3, BUSITYPE, RESERVE4, RESERVE5, RESERVE6, RESERVE7, RESERVE8, RESERVE9, RESERVE10) VALUES ('0827000008', '0827000008"+str(i).zfill(2)+"', '2', '巴中社保批量代发', '511900', '"+str(data_list[0])[0:6]+"', '"+data_list[4]+"', '"+data_list[3]+"', '"+data_list[2]+"', '"+data_list[4][0:4]+"', '1', '1', '20181114113648', '2018-11-06-09.07.34.336389', 'SS', '0', null, null, null, null, null, null);\n")
    index += 1
file.close()
