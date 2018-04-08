#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-03 08:03:53
# @Author  : youanan (youanan@163.com)
# @Link    : youanan.com

'''
使用urllib 爬取csdn首页的所有链接

'''
import re
import urllib.request

def getlink(url):
	#模拟成浏览器
	headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    #根据需要求构建好链接提取表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat),findall(data)
    #去重
    link = list(set(link))
    return link

#要爬取的网页链接
url = "http://blog.csdn.net/"
#获取对应网页中的包含的链接地址
linklist = getlink(url)

for link in linklist:
	print(link[0])
	