#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
引入 lxml 包利用xpath 解析网页
参考：https://www.cnblogs.com/gaochsh/p/6757475.html
'''


# from lxml import etree
# html="""
#     <body>
#         <div id="aa">aa</div>
#         <div id="ab">ab</div>
#         <div id="ac">ac</div>
#     </body>
#     """
# selector=etree.HTML(html)
# content=selector.xpath('//div[starts-with(@id,"a")]/text()') #这里使用starts-with方法提取div的id标签属性值开头为a的div标签
# for each in content:
#     print(each)

#输出结果为：
#aa
# ab
# ac
import urllib
from urllib import request
from lxml import etree
from sys import argv

url = 'http://dict.youdao.com/w/eng/{}/#keyfrom=dict2.index'
word = argv[1]
word = urllib.parse.quote(word)     # 这里处理中文，否则 输入中文会有问题。

turl = url.format(word)
#turl = urllib.parse.quote(turl, safe='/:?=')

with request.urlopen(turl) as f:
    data = f.read()                 # 读取数据 注意数据返回 bytes
    selector = etree.HTML(data)     # 生成 selector  对象
    content = selector.xpath("//div[@id='results-contents']")[0]
    content = etree.tostring(content, encoding='utf-8',method='html')
                                    # 这里利用 etree.tostring() 转换为字符串参考：
                                    # http://lxml.de/api/lxml.etree-module.html
                                    # 注意xpath 的选择器 以及text() 都不能返回html
    print(content.decode('utf-8'))
