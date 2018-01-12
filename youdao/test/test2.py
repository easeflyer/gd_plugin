'''
Created on 2011-11-11

@author: PaulWang

Description:
'''
#import urllib.request,urllib.parse
#
#import http.client
#
#params = urllib.parse.urlencode({'@email': '112233@gmail.com', '@password': '1212123', '@action': 'https://system.netsuite.com/app/login/nllogin.nl'})
#headers = {"Content-type": "application/x-www-form-urlencoded"}
#
#
#conn = http.client.HTTPConnection("www.netsuite.com")
#conn.request("POST", "",params,headers)
#r1 = conn.getresponse()
#print(r1.status, r1.reason)
#data = r1.read()
#print(data)
#conn.close()

import urllib
import sys
import http.cookiejar
#import MutiThreadDown

cookie = http.cookiejar.CookieJar()                                        #保存cookie，为登录后访问其它页面做准备
cjhdr  =  urllib.request.HTTPCookieProcessor(cookie)             
opener = urllib.request.build_opener(cjhdr)


url = "https://system.netsuite.com/pages/customerlogin.jsp?country=US"
postdata = urllib.parse.urlencode({'email': 'yicui49@gmail.com', 'password': 'fashlets123', 'Submit':''})
postdata = postdata.encode('utf-8')

req = urllib.request.Request(url,postdata)
res = urllib.request.urlopen(req)
print(res.status, res.reason)
print(res.read().decode('utf-8'))
# if( res.status != 200 ):
#     exit()

# print('ok')

# url = "https://system.netsuite.com/core/media/media.nl?id=32486&c=776164&h=686103757f3df97d4a92"
# output = '1234567.jpg'

#MutiThreadDown.download( url, output, blocks=1, proxies={} )#自己封装的下载类


