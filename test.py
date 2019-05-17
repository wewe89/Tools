
import re
info='''//#DWR-INSERT
//#DWR-REPLY
var s0=[];var s1={};var s2={};var s3={};var s4={};var s5={};var s6={};var s7={};var s8={};var s9={};var s10={};s0[0]=s1;s0[1]=s2;s0[2]=s3;s0[3]=s4;s0[4]=s5;s0[5]=s6;s0[6]=s7;s0[7]=s8;s0[8]=s9;s0[9]=s10;
s1['TLR_TYPE']="2";s1['OFER_DATE']="2009-01-01";s1['TLR_PAPER_NO']="972717000000000000";s1['CLS_DATE']="2025-12-31";s1['CARD_COND']="0";s1['WORKS_NO']="TLR0A,";s1['SET_DATE']="2009-01-01";s1.CONDITION="2";s1['INST_NO']="7720";s1['TLR_NO']="972717";s1['TLR_NAME']="ATM972717";s1['TLR_LVL']="1";s1['SET_TLR']="999999";
s2['TLR_TYPE']="2";s2['OFER_DATE']="2009-01-01";s2['TLR_PAPER_NO']="972718000000000000";s2['CLS_DATE']="2025-12-31";s2['CARD_COND']="0";s2['WORKS_NO']="TLR0A,";s2['SET_DATE']="2009-01-01";s2.CONDITION="0";s2['INST_NO']="7730";s2['TLR_NO']="972718";s2['TLR_NAME']="ATM972718";s2['TLR_LVL']="1";s2['SET_TLR']="999999";
s3['TLR_TYPE']="2";s3['OFER_DATE']="2009-01-01";s3['TLR_PAPER_NO']="982797000000000000";s3['CLS_DATE']="2025-12-31";s3['CARD_COND']="0";s3['WORKS_NO']="TLR0A,";s3['SET_DATE']="2009-01-01";s3.CONDITION="0";s3['INST_NO']="7723";s3['TLR_NO']="982797";s3['TLR_NAME']="ATM982797";s3['TLR_LVL']="1";s3['SET_TLR']="999999";
s4['TLR_TYPE']="2";s4['OFER_DATE']="2009-01-01";s4['TLR_PAPER_NO']="982798000000000000";s4['CLS_DATE']="2025-12-31";s4['CARD_COND']="0";s4['WORKS_NO']="TLR0A,";s4['SET_DATE']="2009-01-01";s4.CONDITION="0";s4['INST_NO']="7575";s4['TLR_NO']="982798";s4['TLR_NAME']="ATM982798";s4['TLR_LVL']="1";s4['SET_TLR']="999999";
s5['TLR_TYPE']="2";s5['OFER_DATE']="2009-01-01";s5['TLR_PAPER_NO']="984201000000000000";s5['CLS_DATE']="2025-12-31";s5['CARD_COND']="0";s5['WORKS_NO']="TLR0A,";s5['SET_DATE']="2009-01-01";s5.CONDITION="0";s5['INST_NO']="7575";s5['TLR_NO']="984201";s5['TLR_NAME']="ATM984201";s5['TLR_LVL']="1";s5['SET_TLR']="999999";
s6['TLR_TYPE']="2";s6['OFER_DATE']="2009-01-01";s6['TLR_PAPER_NO']="984202000000000000";s6['CLS_DATE']="2025-12-31";s6['CARD_COND']="0";s6['WORKS_NO']="TLR0A,";s6['SET_DATE']="2009-01-01";s6.CONDITION="0";s6['INST_NO']="7575";s6['TLR_NO']="984202";s6['TLR_NAME']="ATM984202";s6['TLR_LVL']="1";s6['SET_TLR']="999999";
s7['TLR_TYPE']="2";s7['OFER_DATE']="2009-01-01";s7['TLR_PAPER_NO']="972719000000000000";s7['CLS_DATE']="2025-12-31";s7['CARD_COND']="0";s7['WORKS_NO']="TLR0A,";s7['SET_DATE']="2009-01-01";s7.CONDITION="0";s7['INST_NO']="7723";s7['TLR_NO']="972719";s7['TLR_NAME']="ATM972719";s7['TLR_LVL']="1";s7['SET_TLR']="999999";
s8['TLR_TYPE']="2";s8['OFER_DATE']="2009-01-01";s8['TLR_PAPER_NO']="972720000000000000";s8['CLS_DATE']="2025-12-31";s8['CARD_COND']="0";s8['WORKS_NO']="TLR0A,";s8['SET_DATE']="2009-01-01";s8.CONDITION="0";s8['INST_NO']="7748";s8['TLR_NO']="972720";s8['TLR_NAME']="ATM972720";s8['TLR_LVL']="1";s8['SET_TLR']="999999";
s9['TLR_TYPE']="2";s9['OFER_DATE']="2009-01-01";s9['TLR_PAPER_NO']="972721000000000000";s9['CLS_DATE']="2025-12-31";s9['CARD_COND']="0";s9['WORKS_NO']="TLR0A,";s9['SET_DATE']="2009-01-01";s9.CONDITION="0";s9['INST_NO']="7575";s9['TLR_NO']="972721";s9['TLR_NAME']="ATM972721";s9['TLR_LVL']="1";s9['SET_TLR']="999999";
s10['TLR_TYPE']="2";s10['OFER_DATE']="2009-01-01";s10['TLR_PAPER_NO']="972722000000000000";s10['CLS_DATE']="2025-12-31";s10['CARD_COND']="0";s10['WORKS_NO']="TLR0A,";s10['SET_DATE']="2009-01-01";s10.CONDITION="0";s10['INST_NO']="7575";s10['TLR_NO']="972722";s10['TLR_NAME']="ATM972722";s10['TLR_LVL']="1";s10['SET_TLR']="999999";
dwr.engine._remoteHandleCallback('2','0',{data:s0,offect:0,pagesize:0});
dwr.engine._remoteHandleCallback('2','1',3020);'''
value={}
i=1
while (i!=0):
    pat=r's'+str(i)+r'''\['(.*?)'\]="(.*?)"'''
    customlist=re.findall(pat,info)
    if(len(customlist)==0):
        i=0
        break
    list={}
    for l in customlist:
        list[l[0]]=l[1]
        value[i-1]=list
    i=i+1
    print(customlist)
for index in value:
    if (int(value[index]['INST_NO']) >= 7571 | int(value[index]['INST_NO']) <= 7703):
        # if (int(value[index]['INST_NO']) != 7702 | int(value[index]['INST_NO']) != 7575):
        #     if (value[index]['TLR_LVL'] == 4):
                print(int(value[index]['INST_NO']), "-----", value[index]['TLR_NO'])
print(value)
# pat=r'''s([1-9]|10)\['INST_NO'\]="(.*?)"'''
# customlist=re.findall(pat,info)
# print(customlist)
# for list in customlist:
#     print(list[1])