'''
ulrlib URLError实战

'''

import urllib.request
import urllib.error

try:
    html = urllib.request.urlopen("http://blog.csdn.net")
    data = html.read()
    print(len(data))
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)
