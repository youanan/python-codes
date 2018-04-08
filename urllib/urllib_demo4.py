'''
urllib 超时设置
'''
import urllib.request
for i in range(1,5):
	try:
		file = urllib.request.urlopen("http://yum.iqianyue.com",timeout=0.01)
		data = file.read()
		print(len(data))
	except Exception as e:
		print("出现异常-->" + str(e))
