'''
http POST请求
1，设置到URL网址
2，构建表单数据，并使用urllib.parse.urlencode对数据进行编码处理
3，创建Request对象，参数包括url网址和传递的数据
4，使用add_header()添加头信息
5, 使用urllib.request.urlopen()打开Request对象，完成信息传递
6, 处理网页内容
'''
import urllib.request

url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
	"name":"youanan",
	"pass":"123456"
	}).encode('utf-8')   #将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
req = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
data = urllib.request.urlopen(req).read()

with open("urllib_posttest.html","wb") as f:
	f.write(data)
	f.close()