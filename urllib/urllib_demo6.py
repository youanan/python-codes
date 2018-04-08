'''
http get请求,中文字符编码时
'''
import urllib.request
key = "爬虫"
key_code = urllib.request.quote(key)
url = "http://www.baidu.com/s?wd="
url_all = url+key_code
req = urllib.request.Request(url_all)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

data = urllib.request.urlopen(req).read()

with open("urllib_baidukeywd2.html","wb") as f:
	f.write(data)
	f.close()