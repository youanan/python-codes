# -*- coding: utf-8 -*-

"""
版本: python 2.76

"""
import urllib

url = "http://www.youanan.com/"
#url = "http://www.163.com/"

html = urllib.urlopen(url)

#print html.read()

print html.info()

