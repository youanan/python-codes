'''
方法2，使用add_header()添加报头
'''
import urllib.request
url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
# headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

req = urllib.request.Request(url)  
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
data = urllib.request.urlopen(req).read()

with open("urllib_csdn.html","wb") as f:
	f.write(data)
	f.close()
