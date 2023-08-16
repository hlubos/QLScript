# -*- coding: utf-8 -*-
"""
cron: 1 6,22 * * *
new Env('微信阅读');

微信捉包 http://7zi1kbpexl.qqaas.fun/app/read/get v域名请求头里的 cookie

青龙变量 export wxread="authtoken=eyJ0eXAiOiJKV1QiLCJhbxxxxx; snapshot=0" 多账号@隔开
"""
import requests
import logging
import time
import os, re
from notify import send

# 创建日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

cookies = []
try:
    if "wxread" in os.environ:
        cookies = os.environ["wxread"].split("@")
        if len(cookies) > 0:
            logger.info(f"共找到{len(cookies)}个账号 已获取并使用Env环境Cookie")
            logger.info("声明：本脚本为学习python 请勿用于非法用途")
    else:
        logger.info("【提示】变量格式: authtoken=eyJ0eXAiOiJKV1QiLCJhbxxxxx; snapshot=0\n环境变量添加: wxread")
        exit(3)
except Exception as e:
    logger.error(f"发生错误：{e}")
    exit(3)


# -------------------------分割线------------------------
class miniso:
    @staticmethod
    def setHeaders(i):
        headers = {
            # 'Host': 'activity.miniso.com',
            'X-Requested-With': 'com.tencent.mm',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; OPPO R9s Build/NZH54D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/5197 MMWEBSDK/20230701 MMWEBID/1571 MicroMessenger/8.0.40.2420(0x2800283F) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
            'Referer': 'http://7zi1kbpexl.qqaas.fun/app/main?openId=oiDdr593RWTMtHI77zdTAvdwsZ5g',
            'cookie': cookies[i]
        }
        return headers

    @staticmethod
    def geturl(headers):
        try:
            url = f'http://7zi1kbpexl.qqaas.fun/app/read/get'
            response = requests.get(url=url, headers=headers)
            result = response.json()
            if result['code'] == 0:
                id = re.search(r'u=(\w+)', result['data']['location']).group(1)
                res = f"获取阅读url: 成功"
                logger.info(res)
                log_list.append(res)
                time.sleep(3)  # 休眠3秒
                miniso.doRead(headers, id)
            else:
                res = f"获取url: 失败"
                logger.info(res)
                log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def doRead(headers, id):
        try:
            url = f'https://sss.mvvv.fun/app/task/doRead?u={id}&type=1'
            response = requests.get(url=url, headers=headers)
            result = response.json()
            if result['code'] == 0:
                taskKey = result['data']['taskKey']
                res = f"获取参数: 成功"
                logger.info(res)
                log_list.append(res)
                time.sleep(10)  # 休眠10秒
                miniso.Read(headers, id, taskKey)
            else:
                res = f"获取参数: 失败"
                logger.info(res)
                log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def Read(headers, id, taskKey):
        try:
            url = f'https://sss.mvvv.fun/app/task/doRead?u={id}&type=1&key={taskKey}'
            response = requests.get(url=url, headers=headers)
            result = response.json()
            if result['code'] == 0:
                taskKey = result['data']['taskKey']
                res = f"阅读: {result['data']['detail']}"
                logger.info(res)
                time.sleep(20)  # 休眠20秒
                miniso.Read(headers, id, taskKey)
            else:
                res = f"阅读: {result['mag']}"
                logger.info(res)
                log_list.append(res)
        except Exception as e:
            print(e)

    @staticmethod
    def my(headers):
        try:
            url = f'http://qmctk1sfcw.qqaas.fun/app/user/myInfo'
            response = requests.get(url=url, headers=headers)
            result = response.json()
            res = f"资产: {result['data']['nameNick']} 金币: {result['data']['goldNow']}"
            logger.info(res)
            log_list.append(res)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    log_list = []  # 存储日志信息的全局变量
    for i in range(len(cookies)):
        logger.info(f"\n开始第{i + 1}个账号")

        logger.info("--------------任务开始--------------")
        headers = miniso.setHeaders(i)
        miniso.geturl(headers)

        miniso.my(headers)

    logger.info("\n============== 推送 ==============")
    send("微信阅读", '\n'.join(log_list))
