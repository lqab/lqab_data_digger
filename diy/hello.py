#!/usr/bin/env python
# -*- coding: UTF-8 -*-  

'''
{
"版权":"LQAB工作室",
"author":{
"1":"集体",
}
"初创时间:"2017年3月",
}
'''

#--------- 外部模块处理<<开始>> ---------#

#-----系统自带必备模块引用-----

import sys # 操作系统模块1
import os # 操作系统模块2
import types # 数据类型
import time # 时间模块
import datetime # 日期模块

#-----系统外部需安装库模块引用-----


#-----DIY自定义库模块引用-----
sys.path.append("..") 
import config #系统配置参数

#--------- 外部模块处理<<结束>> ---------#


#--------- 内部模块处理<<开始>> ---------#

# ---外部参变量处理

# ---全局变量处理

#子目录夹补丁，需人工指定

name_soft = config.dic_config["name_soft"]
# ---本模块内部类或函数定义区
def run_it():

    print("hello world,we are '" + name_soft + "',welcome!" ) # 调试用

#--------- 内部模块处理<<结束>> ---------#

#---------- 主过程<<开始>> -----------#

def main():
    #1 过程一
    run_it()
    #2 过程二
    #3 过程三
    
if __name__ == '__main__':
    main()
    
#---------- 主过程<<结束>> -----------#