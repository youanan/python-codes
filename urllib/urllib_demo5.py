'''
http get请求,英文字符编码时
'''
import urllib.request
keywd = "hello"
url = "http://www.baidu.com/s?wd=" + keywd
req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

data = urllib.request.urlopen(req).read()

with open("urllib_baidukeywd.html","wb") as f:
	f.write(data)
	f.close()