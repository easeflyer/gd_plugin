#coding: utf-8
import time
import random
import hashlib
import requests


while(1):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='

    content = input('输入>>>: ')

    s = "AUTO",
    l = "AUTO"
    u = 'fanyideskweb'
    c = 'rY0D^0\'nM0}g5Mm1z%1G4'
    d = content
    f = str(int(time.time()*1000)+random.randint(1,10))
    sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()

    headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection':'keep-alive',
    'Content-Length':'205',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'JSESSIONID=aaalHNVSigPD8-hsnhf3v; SESSION_FROM_COOKIE=fanyiweb; OUTFOX_SEARCH_USER_ID=526401539@113.16.65.153; _ntes_nnid=1892114ba72ae7f868a29a4db02914a0,1502250589343; _dict_cpm_show=1502250589350; _dict_cpm_close=1; OUTFOX_SEARCH_USER_ID_NCOO=1688640113.572293; ___rl__test__cookies=1502251640921',
    'Host':'fanyi.youdao.com',
    'Origin':'http://fanyi.youdao.com',
    'Referer':'http://fanyi.youdao.com/',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    }

    data = {}
    data['i']=content
    data['from']=s
    data['to']=l
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']=f
    data['sign']=sign
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLlCKBUTTON'
    data['typoResult']='true'

    res = requests.post(url, data, headers=headers)
    print(res.text)