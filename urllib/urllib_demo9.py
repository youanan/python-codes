'''
ulrlib DebugLog实战
1，分别使用urllib.request.HTTPHandler()和urllib.request.HTTPSHandler()将debuglevel设置为1
2, 使用urllib.request.build_opener()创建自定义opener对象,并使用1中的值为参数
3，用urllib.request.install_opener()创建全局默认opener对象,这样，在使用urlopen()时会使用opener对象
4, 进行后续相应操作，如urlopen()'''

import urllib.request
httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen("http://edu.51cto.com")
