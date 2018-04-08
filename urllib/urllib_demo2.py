##
"""
方法1，使用build_opener()修改 请求报头
"""
import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
opener = urllib.request.build_opener()  #创建自定义的opener对象
opener.addheaders = [headers]  #设置头信息,格式:opener 对象名.addheaders = [头信息]
data = opener.open(url).read()  #用opener对象的open方法，格式:opener 对象名.open(url地址)

with open("urllib_csdn.html","wb") as f:
	f.write(data)
	f.close()