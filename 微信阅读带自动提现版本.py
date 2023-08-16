import requests #line:1
import re #line:2
import random #line:3
import time #line:4
from urllib .parse import urlparse ,parse_qs #line:5
from Crypto .Cipher import AES #line:6
import base64 #line:7
def aes_encrypt (OOO00OO0000OO00O0 ):#line:8
    OOO00000O000OO000 =AES .block_size #line:9
    O0000O00OOO000O0O =lambda O0OOO00OO0O00O0OO :O0OOO00OO0O00O0OO +(OOO00000O000OO000 -len (O0OOO00OO0O00O0OO )%OOO00000O000OO000 )*chr (OOO00000O000OO000 -len (O0OOO00OO0O00O0OO )%OOO00000O000OO000 )#line:10
    O000O0000O0O00OO0 =AES .new (b'5e4332761103722eb20bb1ad53907c6e',AES .MODE_ECB )#line:11
    O0000OOO00OOO00OO =O000O0000O0O00OO0 .encrypt (O0000O00OOO000O0O (OOO00OO0000OO00O0 ).encode ())#line:12
    OOO00OOOO0O00O0O0 =str (base64 .b64encode (O0000OOO00OOO00OO ),encoding ='utf-8')#line:13
    return OOO00OOOO0O00O0O0 #line:14
class WXYD :#line:15
    def __init__ (OOOO000OOO00O00OO ,O0O0OOO0000O000OO ):#line:16
        OOOO000OOO00O00OO .homeHost =OOOO000OOO00O00OO .get_readHome ()#line:17
        OOOO000OOO00O00OO .headers ={'Host':OOOO000OOO00O00OO .homeHost ,'Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','token':'','Accept':'*/*','Referer':f'http://{OOOO000OOO00O00OO.homeHost}/app/main?openId=oiDdr54Nefy0xxsTr6SGgdSzpWj0','Accept-Encoding':'gzip, deflate','Accept-Language':'zh-CN,zh','Cookie':f'authtoken={O0O0OOO0000O000OO["authtoken"]}; snapshot=0',}#line:28
    def get_readHome (O00O0O0OOOO00O0OO ):#line:30
        O00OOOO0000O0O00O ={'Host':'sss.mvvv.fun','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','Accept':'*/*','Origin':'https://entry-1318684421.cos.ap-nanjing.myqcloud.com','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://entry-1318684421.cos.ap-nanjing.myqcloud.com/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:43
        OO0OO000OOO0OO0OO ='https://sss.mvvv.fun/app/enter/read_home'#line:44
        O00OO00OOO0O00OOO =requests .get (OO0OO000OOO0OO0OO ,headers =O00OOOO0000O0O00O )#line:45
        print (O00OO00OOO0O00OOO .text )#line:46
        OO00O0O000OO00000 =O00OO00OOO0O00OOO .json ()#line:47
        if OO00O0O000OO00000 .get ('code')==0 :#line:48
            OO0OOOOO000O0OO00 =OO00O0O000OO00000 ['data']['location']#line:49
            O00OOOOOO000OOOOO =re .findall ('//(.*?)/',OO0OOOOO000O0OO00 )[0 ]#line:50
            print ('get home url is',OO0OOOOO000O0OO00 )#line:51
            print ('-'*50 )#line:52
            return O00OOOOOO000OOOOO #line:53
        else :#line:54
            print ('get home page err')#line:55
            return "http://5x034gb8z4.qqaas.fun"#line:56
    def myPickInfo (OOO00OOOOO0OO0O0O ):#line:58
        print ('-'*30 )#line:59
        OOO000OO00O00OOOO =f'http://{OOO00OOOOO0OO0O0O.homeHost}/app/user/myPickInfo'#line:60
        OOO0O0OOO0O00O00O =requests .get (OOO000OO00O00OOOO ,headers =OOO00OOOOO0OO0O0O .headers )#line:61
        OO0O00O0OO0OO0O00 =OOO0O0OOO0O00O00O .json ()#line:62
        print (OOO0O0OOO0O00O00O .text )#line:63
        OO0OO0000O0OOO0OO =OO0O00O0OO0OO0O00 .get ('data')#line:64
        OO00OO0OO0OO0OO00 =OO0OO0000O0OOO0OO .get ('goldNow')#line:65
        if OO00OO0OO0OO0OO00 >0 :#line:66
            O0000OOOO0OO000OO ='http://mhxbn1se67.qqaas.fun/app/user/pickAuto'#line:67
            O00O0O0OOO00O00OO ='{"moneyPick":goldNow}'.replace ('goldNow',str (OO00OO0OO0OO0OO00 ))#line:68
            OO000OOOOOOOOOOOO =aes_encrypt (O00O0O0OOO00O00OO )#line:69
            OOO00OOOOO0OO0O0O .headers .update ({'Content-Type':'application/json'})#line:70
            OOO0O0OOO0O00O00O =requests .post (O0000OOOO0OO000OO ,headers =OOO00OOOOO0OO0O0O .headers ,json =OO000OOOOOOOOOOOO )#line:71
            print ('提现结果',OOO0O0OOO0O00O00O .text )#line:72
        else :#line:73
            print ('没有达到提现标准')#line:74
    def myInfo (OO00OO00000000O0O ):#line:76
        OOO0O0O00O00O0OO0 =f'http://{OO00OO00000000O0O.homeHost}/app/user/myInfo'#line:77
        O000OO000OOOOO0OO =requests .get (OOO0O0O00O00O0OO0 ,headers =OO00OO00000000O0O .headers )#line:78
        O0000OOOO00O0OOOO =O000OO000OOOOO0OO .json ()#line:79
        print (O000OO000OOOOO0OO .text )#line:80
        O0OOO0O0O0OOO0O0O =O0000OOOO00O0OOOO .get ('data')#line:81
        O0OOO0OO0OO0OOO00 =O0000OOOO00O0OOOO .get ('success')#line:82
        O0O0O000OOO0O000O =O0OOO0O0O0OOO0O0O .get ('nameNick')#line:83
        OO00OO00000000O0O .goldNow =O0OOO0O0O0OOO0O0O .get ('goldNow')#line:84
        requests .get (OO00OO00000000O0O .headers .get ('Referer'),headers =OO00OO00000000O0O .headers )#line:85
        OOO00OOO00OOO0O00 =O0OOO0O0O0OOO0O0O .get ('completeTodayCount')#line:86
        OOOO0O0OOO0000O0O =O0OOO0O0O0OOO0O0O .get ('completeTodayGold')#line:87
        OOOO0OOOO0OOO00O0 =O0OOO0O0O0OOO0O0O .get ('readable')#line:88
        OO00OO0OOO0OOOOO0 =O0OOO0O0O0OOO0O0O .get ('remainSec')#line:89
        print (f'当前用户{O0O0O000OOO0O000O}，当前积分:{OO00OO00000000O0O.goldNow}，今日已读{OOO00OOO00OOO0O00}篇文章，获得了{OOOO0O0OOO0000O0O}积分，用户状态:{OOOO0OOOO0OOO00O0},提示信息:{O0OOO0OO0OO0OOO00}。')#line:91
        if OO00OO0OOO0OOOOO0 ==0 :#line:92
            print ('当前是读文章的状态')#line:93
        else :#line:94
            O0OOOO0O000000O00 =int (OO00OO0OOO0OOOOO0 /60 )#line:95
            print ('当前不是是读文章的状态,距离下次阅读还有',O0OOOO0O000000O00 ,'分钟')#line:96
            return False #line:97
        print ('-'*50 )#line:98
        return True #line:99
    def getkey (O0O0OO00O0O000O00 ):#line:101
        O000OO00O0OOO00OO =f'http://{O0O0OO00O0O000O00.homeHost}/app/read/get'#line:102
        OOO0O0OOOO0O0OO00 =requests .get (O000OO00O0OOO00OO ,headers =O0O0OO00O0O000O00 .headers )#line:103
        OOOO0OOOOO0O0OO0O =OOO0O0OOOO0O0OO00 .json ()#line:104
        print (OOO0O0OOOO0O0OO00 .text )#line:105
        OO000O0000O0O0OOO =OOOO0OOOOO0O0OO0O .get ('data').get ('location')#line:106
        O00OOO00000O00O0O =parse_qs (urlparse (OO000O0000O0O0OOO ).query )#line:107
        OO00OOO00OO0OO0OO =urlparse (OO000O0000O0O0OOO )#line:108
        OO0OO00O0O0000000 =O00OOO00000O00O0O .get ('u')[0 ]#line:109
        print ('get key is ',OO0OO00O0O0000000 )#line:110
        print ('-'*50 )#line:111
        OO0OO0OO0O0O0OOOO =f'https://sss.mvvv.fun/app/task/doRead?u={OO0OO00O0O0000000}&type=1'#line:112
        OO00000000O00OO0O ={'Host':'sss.mvvv.fun','Connection':'keep-alive','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090621) XWEB/8351 Flue','X-Requested-With':'XMLHttpRequest','Accept':'*/*','Origin':f'https://{OO00OOO00OO0OO0OO}','Sec-Fetch-Site':'cross-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':f'https://{OO00OOO00OO0OO0OO}/','Accept-Encoding':'gzip, deflate, br','Accept-Language':'zh-CN,zh',}#line:126
        O0OOO0O0O00OOOO0O =requests .get (OO0OO0OO0O0O0OOOO ,headers =OO00000000O00OO0O )#line:127
        print (O0OOO0O0O00OOOO0O .text )#line:128
        O0OO00O000O000O0O =O0OOO0O0O00OOOO0O .json ()#line:129
        if O0OO00O000O000O0O .get ('code')==0 :#line:130
            OOOO0O0O0O00OOO0O =O0OO00O000O000O0O .get ('data').get ('taskKey')#line:131
            OOO0OO0O000OO00OO =O0OO00O000O000O0O .get ('data').get ('bizCode')#line:132
            if OOO0OO0O000OO00OO ==20 :#line:133
                print ('The article is being updated. Please try again later.')#line:134
                return False #line:135
            if OOOO0O0O0O00OOO0O ==None :#line:136
                print ()#line:137
                return False #line:138
            print ('this task key is ',OOOO0O0O0O00OOO0O )#line:139
            print ('-'*50 )#line:140
            O00OOOO000000OO0O =random .randint (10 ,15 )#line:141
            print (f'本次模拟读{O00OOOO000000OO0O}秒')#line:142
            print ('-'*50 )#line:143
            time .sleep (O00OOOO000000OO0O )#line:144
            return OOOO0O0O0O00OOO0O ,OO0OO00O0O0000000 ,OO00000000O00OO0O #line:145
        else :#line:146
            print ('get taskKey err')#line:147
            print ('-'*50 )#line:148
            return False #line:149
    def do_read (OOOO0O0000O000OOO ):#line:151
        O000000OOO0O0O00O =OOOO0O0000O000OOO .getkey ()#line:152
        if O000000OOO0O0O00O ==False :#line:153
            print ('read wenzhang err')#line:154
            return False #line:155
        OOOO0O0000O000OOO .taskKey =O000000OOO0O0O00O [0 ]#line:156
        while True :#line:157
            OO0OOO0O0OOO000OO =f'https://sss.mvvv.fun/app/task/doRead?u={O000000OOO0O0O00O[1]}&type=1&key={OOOO0O0000O000OOO.taskKey}'#line:158
            OOOOOOO0OO00O000O =requests .get (OO0OOO0O0OOO000OO ,headers =O000000OOO0O0O00O [2 ])#line:159
            print (OOOOOOO0OO00O000O .text )#line:160
            OO0OOO0O0000OO0OO =OOOOOOO0OO00O000O .json ()#line:161
            if OO0OOO0O0000OO0OO .get ('code')!=0 :#line:162
                break #line:163
            O00O00OO0OO00O0OO =OO0OOO0O0000OO0OO .get ('data').get ('detail')#line:164
            print (f'上次一篇阅读结果：{O00O00OO0OO00O0OO}')#line:165
            OOOO0O0000O000OOO .taskKey =OO0OOO0O0000OO0OO .get ('data').get ('taskKey')#line:166
            print ('this task key is ',OOOO0O0000O000OOO .taskKey )#line:167
            if OOOO0O0000O000OOO .taskKey ==None :#line:168
                break #line:169
            OO0OO0OO0O000OO00 =random .randint (10 ,15 )#line:170
            print (f'本次模拟读{OO0OO0OO0O000OO00}秒')#line:171
            print ('-'*50 )#line:172
            time .sleep (OO0OO0OO0O000OO00 )#line:173
        print ('read over')#line:174
    def run (O0O000OOOO00O00OO ):#line:176
        if O0O000OOOO00O00OO .myInfo ():#line:177
            time .sleep (10 )#line:178
            O0O000OOOO00O00OO .do_read ()#line:179
            time .sleep (2 )#line:180
            O0O000OOOO00O00OO .myInfo ()#line:181
        time .sleep (2 )#line:182
        O0O000OOOO00O00OO .myPickInfo ()#line:183
if __name__ =='__main__':#line:185

    # 活动入口,微信打开：https://entry-1318684421.cos.ap-nanjing.myqcloud.com/cos_b.html?openId=oiDdr54Nefy0xxsTr6SGgdSzpWj0

    # 打开活动入口，抓包的任意接口cookies中的authtoken参数

    #定时运行每两小时一次 0 0 1-12/2 * * *

    #自动提现

    # 单账户mycklist=[{'authtoken': 'xxxx'}]

    # 多账户mycklist=[{'authtoken': 'xxxx'},{'authtoken': 'xxxx'},{'authtoken': 'xxxx'},]

    mycklist =[
        {'authtoken': 'xxxx'},
        {'authtoken': 'xxxx'},
    ]#line:193
    for i in mycklist :#line:194
        api =WXYD (i )#line:195
        api .run ()#line:196
        time .sleep (5 )#line:197
