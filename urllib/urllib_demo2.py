##
"""
����1��ʹ��build_opener()�޸� ����ͷ
"""
import urllib.request

url = "http://blog.csdn.net/weiwei_pig/article/details/51178226"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
opener = urllib.request.build_opener()  #�����Զ����opener����
opener.addheaders = [headers]  #����ͷ��Ϣ,��ʽ:opener ������.addheaders = [ͷ��Ϣ]
data = opener.open(url).read()  #��opener�����open��������ʽ:opener ������.open(url��ַ)

with open("urllib_csdn.html","wb") as f:
	f.write(data)
	f.close()