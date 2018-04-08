'''
方法2，使用add_header()添加报头
'''
import urllib.request
url = "http://chart.cp.360.cn/kaijiang/kaijiang?lotId=166406&spanType=2&span=2018-04-04_2018-04-04"
# headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

req = urllib.request.Request(url)  
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
data = urllib.request.urlopen(req).read()

with open("360cp.html","wb") as f:
	f.write(data)
	f.close()
