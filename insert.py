import sys
import io
import json
file = open("营业部.txt", "r")  # 打开文件

file1 = open("营业部1.txt", "w")  # 打开文件

allStr=file.read().replace('\\n', '')

data=json.loads(allStr)["nextgroup"]
for index in range(len(data)):
    line=data[index]["userList"]
    if(line is not None):
        for index1 in range(len(line)):
            str1=line[index1]
            # oneline=str["loginId"]+","+str["mail"]+","+str["mobile"]+","+str(str["userId"])+","+str["userId"]+"/n"
            oneline=json.dumps(str1)
            print(oneline)
            file1.write(str1["loginId"]+","+str1["mail"]+","+str1["mobile"]+","+str(str1["userId"])+","+str(str1["userName"])+'\n')
file1.close()
file.close()  # 关闭文件