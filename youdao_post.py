#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
post 方式提交数据
参考：http://blog.csdn.net/serverxp/article/details/6963059
'''

import urllib,time,random,hashlib,json
from urllib import request
from lxml import etree
from sys import argv


if __name__ == "__main__":
    d = argv[1]
    #d = 'This is a mixin class that helps with HTTP authentication, both to the remote host and to a proxy. password_mgr, if given, should be something that is compatible with HTTPPasswordMgr; refer to section HTTPPasswordMgr Objects for information on the interface that must be supported. If passwd_mgr also provides is_authenticated and update_authenticated methods (see HTTPPasswordMgrWithPriorAuth Objects), then the handler will use the is_authenticated result for a given URI to determine whether or not to send authentication credentials with the request. If is_authenticated returns True for the URI, credentials are sent. If is_authenticated is False, credentials are not sent, and then if a 401 response is received the request is re-sent with the authentication credentials. If authentication succeeds, update_authenticated is called to set is_authenticated True for the URI, so that subsequent requests to the URI or any of its super-URIs will automatically include the authentication credentials. '    
    #d = urllib.parse.quote(d)   
    #d = 'test'
    u = 'fanyideskweb'
    #f = str(int(time.time() * 1000))
    f = str(int(time.time() * 1000) + random.randint(1, 10))
    c = "rY0D^0\'nM0}g5Mm1z%1G4"
    # m = hashlib.md5()
    # m.update((u + d + f + c).encode('utf-8'))
    # sign = m.hexdigest()
    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
    data = {
        'i': d,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': u,
        'salt': f,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_ENTER',
        'typoResult': 'true'
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
       # 'Accept-Encoding': 'gzip, deflate',   # 注意这一行，如果有这一行，返回的响应是压缩的可能不能正常输出
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '205',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'JSESSIONID=aaalHNVSigPD8-hsnhf3v; SESSION_FROM_COOKIE=fanyiweb; OUTFOX_SEARCH_USER_ID=526401539@113.16.65.153; _ntes_nnid=1892114ba72ae7f868a29a4db02914a0,1502250589343; _dict_cpm_show=1502250589350; _dict_cpm_close=1; OUTFOX_SEARCH_USER_ID_NCOO=1688640113.572293; ___rl__test__cookies=1502251640921',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
#        'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
    postdata = urllib.parse.urlencode(data)
    postdata = postdata.encode('utf-8')
    #headers = urllib.parse.urlencode(headers)
    #headers = headers.encode('utf-8')  
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req,data=postdata) 
    
    # json = json.load(res.read())
    # print(json);exit()
    
    #print(res.status, 're:',res.reason)  
    json1 = res.read().decode('utf-8',errors='ignore')
    #print(json1)
    obj1 = json.loads(json1,encoding='utf-8')

    # for res in obj1['translateResult'][0]:
    #     print(res['src'])
    for res in obj1['translateResult'][0]:
        print(res['tgt'],end='')


    #print(obj1['translateResult'][0][0]['src'])
    #print(obj1['translateResult'][0][0]['tgt'])
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