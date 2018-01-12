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
    word = argv[1]
    word = word.replace("/","／")       # url 方式要过滤掉 / 换成全角
    
    d = word
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
        'query': 'test',
        'from': 'en',
        'to': 'zh',
#        'smartresult': 'dict',
#        'client': u,
#        'salt': f,
        'transtype':'translang',
        'sign': '431039.159886',
        'token':'be164775f687f4e870e4948e8d24d0ee'
#        'doctype': 'json',
#        'version': '2.1',
#        'keyfrom': 'fanyi.web',
#        'action': 'FY_BY_ENTER',
#        'typoResult': 'true'
    }

    headers = {
        'Accept': '*/*',
       # 'Accept-Encoding': 'gzip, deflate',   # 注意这一行，如果有这一行，返回的响应是压缩的可能不能正常输出
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '122',
        #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'BAIDUID=221066F4CE811A8879DA2BB0CD405C3B:FG=1; BIDUPSID=221066F4CE811A8879DA2BB0CD405C3B; PSTM=1515382909; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=xQNU5ndWFobEs2SUpFNWZNbWQ3ekNiMm5jUzR-Sk03NThnVzVReXJ5Y3ZXSDFhQVFBQUFBJCQAAAAAAAAAAAEAAACSz7MARWFzZWZseWVyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC~LVVovy1Vaa2; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1515726036,1515736343,1515736780; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=25638_1469_21104_18560_20927; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1515736806',
        'Host': 'fanyi.baidu.com',
        #'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.baidu.com/translate?aldtype=16047&query=test&keyfrom=baidu&smartresult=dict&lang=auto2zh',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        #'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    #url = 'http://correctxt.baidu.com/correctxt?callback=jQuery11130700861234123714_1515729680608&text={}&ie=utf-8&version=0&from=FanyiWeb&_=1515729680609'
    #url = 'http://fanyi.baidu.com/pcnewcollection?req=check&fanyi_src={}&direction=en2zh&_=1515729680610'
    url = 'http://fanyi.baidu.com/v2transapi'
    #url = url.format("test")
    postdata = urllib.parse.urlencode(data)
    postdata = postdata.encode('utf-8')
    #headers = urllib.parse.urlencode(headers)
    #headers = headers.encode('utf-8')  
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req,data=postdata) 
    #res = urllib.request.urlopen(req) 
    
    # json = json.load(res.read())
    # print(json);exit()
    
    #print(res.status, 're:',res.reason)  
    json1 = res.read().decode('utf-8',errors='ignore')
    #print(json1);exit();
    obj1 = json.loads(json1,encoding='utf-8')
    print(obj1['trans_result']['data'][0]['dst']);exit();
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