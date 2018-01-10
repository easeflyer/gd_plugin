#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
post 方式提交数据
参考：http://blog.csdn.net/serverxp/article/details/6963059
'''

import urllib,time,random,hashlib
from urllib import request
from lxml import etree
from sys import argv


if __name__ == "__main__":
    d = 'coroutine'
    u = 'fanyideskweb'
    #f = str(int(time.time() * 1000))
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = "rY0D^0\'nM0}g5Mm1z%1G4"
    # m = hashlib.md5()
    # m.update((u + d + f + c).encode('utf-8'))
    # sign = m.hexdigest()
    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
    data = {
        'id': 'python'
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Host': 'www.ushow.org',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    }
    url = 'http://www.ushow.org/start?do=search'
    postdata = urllib.parse.urlencode(data)
    postdata = postdata.encode('utf-8')
    #headers = urllib.parse.urlencode(headers)
    #headers = headers.encode('utf-8')  
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req,data=postdata) 
    print(res.status, 're:',res.reason)  
    print(res.read().decode('utf-8',errors='ignore'))
    #print(res.read())



# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
# i	翻译软
# from	AUTO
# to	AUTO
# smartresult	dict
# client	fanyideskweb
# salt	1515470355023
# sign	a26df517100efe86ebe72999e4c9c5a7
# doctype	json
# version	2.1
# keyfrom	fanyi.web
# action	FY_BY_REALTIME
# typoResult	false