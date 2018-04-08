'''
ulrlib 使用代理, 测试不成功
'''

def use_porxy(proxy_addr,url):
	'''
    定义一个函数，两个参数，代理地址，访问的URL
	'''
	import urllib.request
	proxy = urllib.request.ProxyHandler({'http':proxy_addr})
	#使用urllib.request.ProxyHandler()来设置代理信息,格式为:urllib.request.ProxyHandler({'http':代理服务器地址})

	opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
	#创建一个opener对象,第一个参数为代理信息，第二个参数为urllib.request.HTTPHandler类

	# urllib.request.install_opener(opener)
    #为了方便，可以使用urllib.request.install_opener()创建全局默认的opener对象
    #那么，在使用urlopen()时亦会使用我们安装的opener对象

	data = opener.open(url).read().decode('utf-8')
	# data = urllib.request.urlopen(url).read().decode('utf-8')
	return data

proxy_addr = "58.19.13.212:18118"
data = use_porxy(proxy_addr,"http://www.youanan.com")
print(len(data))
