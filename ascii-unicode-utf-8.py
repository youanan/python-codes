# ascii-unicode-utf-8.py

'''
 ascii 		存2个字节(不能存汉字)
 unicode 	全部用2个字节保存
 utf-8 		用3个字节保存汉字(用1个字节保存英文)


>>> print ord("0")
48
>>> a = 'alex'
>>> type(a)
<type 'str'>
>>> a = u'alex'
>>> type(a)
<type 'unicode'>

>>> name = u'你好'
>>> name
u'\u4f60\u597d'
>>> print name
你好
>>> len(name)
2
>>> name.encode('utf-8')
'\xe4\xbd\xa0\xe5\xa5\xbd'

'''