'''
re 正则表达式

'''
import re

# pattern = "yue"  #普通字符作为原子
# string = "http://yum.iqianyue.com"   
# resultl = re.search(pattern,string)
# print(resultl)

html = "<a href='http://www.baidu.com'>百度首页</a>"
pattern = "[a-zA-Z]+://[^\s]*[.com|cn]"
resultl = re.search(pattern,html)
print(resultl)