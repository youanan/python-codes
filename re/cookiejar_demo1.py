'''
cookie, 使用cookkiejar模拟登陆

'''
import urllib.request
import urllib.parse
import http.cookiejar

login_url = "https://netgear.opendns.com/sign_in.php"
postdata = urllib.parse.urlencode({
    "username":"youanan",
    "password":"ya1983"
    }).encode('utf-8')  #使用urlencode编码处理后，再设置为utf-8

req = urllib.request.Request(login_url,postdata) #构建request对象
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

#使用http.cookiejar.CookieJar()创建CookieJar对象
cjar = http.cookiejar.CookieJar()

#使用HTTPCookieProcessor创建cookie处理器,并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))

#将opener安装为全局
urllib.request.install_opener(opener)

file = opener.open(req)
data = file.read()  

with open("urllib_logintest.html","wb") as f:
    f.write(data)
    f.close()

url2 = "https://netgear.opendns.com/account.php?device_id=0000578F4A2A6E30&view=timezone"
data2 = urllib.request.urlopen(url2).read()  #登陆并爬取网页

with open("urllib_logintest_page2.html","wb") as f2:
    f2.write(data2)
    f2.close()
