'''
用urllib.request爬取jd手机图片

'''
import urllib.request
import re
import os

def craw(url,page):
    req = urllib.request.Request(url)  
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    html1 = urllib.request.urlopen(req).read()
    html1 = str(html1)

    #第一次过滤
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]

    #第二次过滤
    pat2 = '<img width="220" height="220" data-img="1".*? src="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    for imageurl in imagelist:
        imagename = "img/"+str(page)+str(x)+".jpg"
        imageurl = "https://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1

for i in range(1,10):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)

