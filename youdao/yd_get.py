#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from sys import argv

URL = "http://dict.youdao.com/w/eng/{}/#keyfrom=dict2.index"

def translate(words):
    """函数说明：
    因为采用 get 方式 url 中要过滤掉 / 换成全角。否则引起url的解析错误。
    response.text 是 bytes 数据类型
    """
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
    #headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.67 Chrome/70.0.3538.67 Safari/537.36'}
    words = words.replace("/", "／")       
    url = URL.format(words)

    response = requests.get(url)
    selector = etree.HTML(response.text)     # 生成 selector  对象, 利用 xpath 获得内容
    content = selector.xpath("//div[@id='results-contents']")[0]
    content = etree.tostring(content, encoding='utf-8', method='html')

    result = content.decode('utf-8')
    result = result.replace("<img src", "<img style='float:right;width:30vw' src")       # url 方式要过滤掉 / 换成全角
    return result


if __name__ == "__main__":
    """
    argv[1] 获得控制器输入的第一个参数
    """
    result = translate(argv[1])
    print(result)