def 明细():
    file = open(r'C:\Users\ZHXY\Desktop\回盘\760504201908201051READY00000000000000645235惠民惠农查询.csv', "r",encoding='UTF-8')
    des = open(r'C:\Users\ZHXY\Desktop\回盘\db.sql', "w",encoding='UTF-8')
    for line in file:
        if ("894322" in line) or ("894322" in line) or ("896934" in line) or("837447" in line) or ("900541" in line) or ("901825" in line) or ("901849" in line) or ("901852" in line) or ("901891" in line ):
            line=line.replace(" ","")
            line=line[:line.rindex(",")]
            line=line.replace(",","','")
            # print(line)
            strline="INSERT INTO AFA_BATCH_BATPAYLST (BATCHID, SEQ_NUM, CUST_NO, CUST_NAME, COL_ACC, SIGN_ACC, ACC_TYPE, CERT_TYPE, CERT_ID, HEADNO, VOSTKIND, CERT_NO, ORIG_AMT, LATE_FEE, FEE, COST_DESC, COST_MUST, RB_AMT, REAL_AMT, ADDRESS, PHONE, SUMM_CODE, NOTE, CARD_FLAG, PRTFLG, FLAG, EXP_FLAG, REMARK1, REMARK2, HOST_CODE, TRAN_MSG, CREATEINSTNO, CREATEUSERID, CREATEDATE, CREATEDATETIME, LASTMODIINSTNO, LASTMODIUSERID, LASTMODIDATE, LASTMODIDATETIME, VALUE01, VALUE02, VALUE03, VALUE04, VALUE05, VALUE06, VALUE07, VALUE08, VALUE09, VALUE10, VALUE11, VALUE12, VALUE13, VALUE14, VALUE15, VALUE16, VALUE17, VALUE18, VALUE19, VALUE20, VALUE21, VALUE22, VALUE23, VALUE24, VALUE25, VALUE26, VALUE27, VALUE28, VALUE29, VALUE30, VALUE31, VALUE32, VALUE33, VALUE34, VALUE35, VALUE36, VALUE37, VALUE38, VALUE39, VALUE40, VALUE41, VALUE42, VALUE43, VALUE44, VALUE45, VALUE46, VALUE47, VALUE48, VALUE49, VALUE50, BAK1, BAK2, BAK3) VALUES ('" +line+"');"
            strline=strline.replace("\n","")
            print(strline)
            des.writelines(strline+ "\n")
    file.close()
    des.close()
def 批次():
    file = open(r'C:\Users\ZHXY\Desktop\回盘\afa_batch_batjobreg_20190820.csv', "r",
                encoding='gb2312')
    des = open(r'C:\Users\ZHXY\Desktop\回盘\pici.txt', "w", encoding='gb2312')
    for line in file:
        line = line.replace(" ", "")
        line = line[:line.rindex(",")]
        line = line.replace(",", "','")
        line = line.replace("(null)", "")
        # print(line)
        strline = "INSERT INTO AFA_BATCH_BATJOBREG (CHANNEL_TYPE, BATCH_DESC, BATCHID, FA_BATCHID, CALL_NUM, WORK_STAT, END_STAT, BATCH_TYPE, PRD_CODE, SUB_PRD_CODE, WORK_MODE, THD_BATCHID, SPLIT_FLAG, BEGIN_SEQ_NUM, END_SEQ_NUM, UNIT_TYPE, CALL_DATETIME, RANDOM_CODE, RAWFILENAME, RAWFILEID, RAWFILEDESC, HEAD_ACC, COM_ACC, COM_ACC_NAME, MONEY_TYPE, PAY_MAIN_STAT, WORK_DATE, HOPE_DATE, EXPIRE_DATE, ONEPK_FLAG, IS_OPEN_FLAG, PRDNO, IDENT_FLAG, CHECK_FLAG, HOSTFILENAME, BACKFILENAME, CURR_IDEN, CURR_TYPE, TOTAL_NUM, TOTAL_AMT, SUCC_NUM, SUCC_AMT, FAIL_NUM, FAIL_AMT, SUMM_CODE, NOTE, CTRL_SUMM_CODE, CTRL_NOTE, BATCHLEVEL, TRANSFER_CALL_DATE, TRANSFER_CALL_SEQ, MAIN_CALL_DATE, MAIN_CALL_SEQ, CLEAR_CALL_DATE, CLEAR_CALL_SEQ, HOST_FILE_DATETIME, LIST_PRINT_NUM, CERT_PRINT_NUM, EXCHANGE_ID, EXT_WORK_FLAG, EXT_WORK_STAT, EXT_END_STAT, CLEAR_FLAG, CLEAR_STAT, BACK_FLAG, BACK_FILE, DEALCODE, DEALMSG, DISPATCHMSG, THD_CODE, THD_MESG, INST_NO, TELLER, CHANNEL, TERM_TYPE, SYSDATA01, SYSDATA02, SYSDATA03, DATA01, DATA02, DATA03, DATA04, DATA05, DATA06, DATA07, DATA08, DATA09, DATA10, DATA11, DATA12, DATA13, DATA14, DATA15, DATA16, DATA17, DATA18, DATA19, DATA20, CREATEINSTNO, CREATEUSERID, CREATEDATE, CREATEDATETIME, LASTMODIINSTNO, LASTMODIUSERID, LASTMODIDATE, LASTMODIDATETIME, LOCK_FLAG, LOCK_DATETIME, RESERVE1, RESERVE2, RESERVE3, SYSDATA04, SYSDATA05, SYSDATA06, SYSDATA07, SYSDATA08) VALUES ('"+line+"','');"
        strline = strline.replace("\n", "")
        print(strline)
        des.writelines(strline + "\n")
    file.close()
    des.close()
if __name__ == '__main__':
   明细()