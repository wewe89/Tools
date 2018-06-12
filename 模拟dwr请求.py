import requests
import re
import random
import sys
import time

poitems = [['26621742', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST15041', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8115041'],
           ['26621743', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST16137', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8116137'],
           ['26621744', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST19983', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8119983'],
           ['26621745', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST10941', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8110941'],
           ['26621746', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST17630', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8117630'],
           ['26621747', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST14313', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8114313'],
           ['26621748', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST17901', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8117901'],
           ['26621749', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST13596', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8113596'],
           ['26621750', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST14834', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8114834'],
           ['26621751', 'POPOTEST10002', 'POTEST10002', 'ITEMTEST17821', '%E6%B5%8B%E8%AF%95%E5%95%86%E5%93%8117821']]


class Transaction(object):
    def __init__(self):
        self.custom_timers = {}  # restart timer
        self.ssrequest = requests.session()

    def run(self):

        ##########################   Bussniess    ##########################
        res = ''
        try:

            #######add scan result
            headers = {
                'content-type': 'text/plain',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36'
            }

            url3 = "http://10.128.1.124:8001/scom/dwr/call/plaincall/Multiple.2.dwr"
            private = {
                'callCount':'2',
'page':'/scom/screen/errordispose/dealnoteselect/ledgerlistQuery.jsp?modleid\':\'tradeselect',
'httpSessionId':'y80hbhlXLwcQCRgYnGcdwK8PTQGFF4QTpQNf227KqqVcKytdCp9h!1947543175',
'scriptSessionId':'19EAFF47B7D0D244219E7E2BB2EF8D54128',
'c0-scriptName':'ledgerListQuery',
'c0-methodName':'obtainDataList',
'c0-id':'0',
'c0-param0':'number:0',
'c0-param1':'number:10',
'c0-param2':'null:null',
'c0-e3':'string:LEDGER',
'c0-e4':'string:oper_equal',
'c0-e5':'string:2',
'c0-e6':'string:',
'c0-e2':'Object_Condition:{fieldName:reference:c0-e3, oper:reference:c0-e4, value1:reference:c0-e5, value2:reference:c0-e6}',
'c0-e8':'string:VALUE',
'c0-e9':'string:oper_equal',
'c0-e10':'string:6214571781004507419',
'c0-e11':'string:',
'c0-e7':'Object_Condition:{fieldName:reference:c0-e8, oper:reference:c0-e9, value1:reference:c0-e10, value2:reference:c0-e11}',
'c0-e13':'string:MODLEID',
'c0-e14':'string:oper_equal',
'c0-e15':'string:tradeselect',
'c0-e16':'string:',
'c0-e12':'Object_Condition:{fieldName:reference:c0-e13, oper:reference:c0-e14, value1:reference:c0-e15, value2:reference:c0-e16}',
'c0-e1':'Array:[reference:c0-e2,reference:c0-e7,reference:c0-e12]',
'c0-param3':'Object_And:{conditions:reference:c0-e1}',
'c0-param4':'null:null',
'c1-scriptName':'ledgerListQuery',
'c1-methodName':'getRowCount',
'c1-id':'1',
'c1-e19':'string:LEDGER',
'c1-e20':'string:oper_equal',
'c1-e21':'string:2',
'c1-e22':'string:',
'c1-e18':'Object_Condition:{fieldName:reference:c1-e19, oper:reference:c1-e20, value1:reference:c1-e21, value2:reference:c1-e22}',
'c1-e24':'string:VALUE',
'c1-e25':'string:oper_equal',
'c1-e26':'string:6214571781004507419',
'c1-e27':'string:',
'c1-e23':'Object_Condition:{fieldName:reference:c1-e24, oper:reference:c1-e25, value1:reference:c1-e26, value2:reference:c1-e27}',
'c1-e29':'string:MODLEID',
'c1-e30':'string:oper_equal',
'c1-e31':'string:tradeselect',
'c1-e32':'string:',
'c1-e28':'Object_Condition:{fieldName:reference:c1-e29, oper:reference:c1-e30, value1:reference:c1-e31, value2:reference:c1-e32}',
'c1-e17':'Array:[reference:c1-e18,reference:c1-e23,reference:c1-e28]',
'c1-param0':'Object_And:{conditions:reference:c1-e17}',
'c1-param1':'null:null',
'batchId':'7',

            }
            start = time.time()
            r = self.ssrequest.post(url3, data=private, headers=headers)
            print(r.text)
            response_time = time.time()
            self.custom_timers['response sent'] = response_time - start
            time.sleep(0.01)
            # print r.text
        except Exception as e:
            print
            str(e)
            print
            str(sys.exc_info())
            raise Exception('Error: {0}--{1}--{2}'.format(res.replace('\n', ''), str(e), str(sys.exc_info())))


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
