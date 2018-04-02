#! /usr/bin/env python
'''
本例使用os模块的os.path功能，实现文本目录等操作
'''

#!/usr/bin/env python

import os    #引入os模块
for tmpdir in ('/tmp', r'c:\temp'):    #遍历两个目录
    if os.path.isdir(tmpdir):          #for循环遍历判断以上两个目录是否存在
        break                          #如果存在，tmpdir变量值为其中一个值，退出for循环，下面if条件将为True
else:                                  #如果不存在
    print('temp目录或路径不存在')      #print
    tmpdir = ''                        #设置tmpdir变量的值为空,下面if条件值为False，将全部不执行

if tmpdir:                             #如果条件为True,执行以下代码:                          
    os.chdir(tmpdir)                   #用 os.chdir() 改变目录到tempdir
    cwd = os.getcwd()                  #用 os.getcwd() 获取当前目录
    print('*** 当前的temp目录是：') 
    print(cwd)                         #将当前目录输出打印

    print('*** 创建一个示例目录...')  #创建一个示例目录
    if not os.path.exists('example'): os.mkdir('example')  #如果不存在名称为:"example"目录则创建
    os.chdir('example')                #切换到example目录
    cwd = os.getcwd()                  #获取当前的目录名称
    print('*** 新的示例目录是：')
    print(cwd)                         #将当前目录输出打印

    print('*** 初始目录明细: ')  #初始目录明细
    print(os.listdir(cwd))       #用 os.listdir获取指定目录的文件
    print('*** 创建一个新文件...')  #创建一个新文件
    fobj = open('test1.txt', 'w')        #以写入的模式打开一个文件，名称为text1.txt
    fobj.write('foo\n')             #写入一个foo换行
    fobj.write('bar\n')             #写入一个bar换行
    fobj.close()                    #保存关闭文件
    print('*** 更新后的目录文件:')      
    print(os.listdir(cwd))          #打印输出目录的文件
    
    print('*** 修改"test1.txt" 为 "filetest.txt"')  #将要修改文件名
    os.rename('test1.txt', 'filetest.txt')               #用 os.rename 修改文件名
    print('*** 再次更新目录文件: ')
    print(os.listdir(cwd))            #再次打印输出目录文件

    path = os.path.join(cwd, os.listdir(cwd)[0])   #变量=合并路径(当前目录路径+路径首个文件名)
    print('*** 完整的路径及文件名：')   #完整的路径及文件名
    print(path)                         #输出刚才的变量值
    print('*** (路径名, basename) ==')  #分开输出路径名，文件名
    print(os.path.split(path))
    print('*** (文件名, extension) ==') #分开输出文件名，后缀名
    print(os.path.splitext(os.path.basename(path)))

    print('*** 显示文件内容:')
    fobj = open(path)
    for eachLine in fobj:
        print(eachLine,)
    fobj.close()

    print('*** 删除测试文件')
    os.remove(path)
    print('*** 更新目录列表: ')
    print(os.listdir(cwd))       #输出更新后的目录文件
    os.chdir(os.pardir)          #改变目录到父级目录
    print('*** 删除测试目录')  
    os.rmdir('example')          #删除 example目录
    print('*** 示例完成')            
