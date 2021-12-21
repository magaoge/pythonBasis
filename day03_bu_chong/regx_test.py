# -*- coding: utf-8 -*-
# @Time    : 2021/12/21 1:25 下午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : regx_test.py
# @Software: PyCharm

import re

# 声明字符串
s = "www.lemfix.com"

# -------------match函数:
# 作用：是匹配字符串
# 规则：从字符串的头部开始匹配
# 用法：match("匹配规则",目标字符串)
# 返回数据类型：对象内存地址

res = re.match("www",s)
print(res)#输出的是内存地址
print(res.group())#输出的是匹配到的全字符串结果

# ---------------match+group函数:
# 作用：是匹配字符串，并对结果进行分组
# 规则：无分组规则时，和match规则相同从字符串的头部开始匹配，有规则时以下讲解
# 用法：match("（匹配规则1），（匹配规则2）",目标字符串)
# 返回数据类型：对象内存地址

res = re.match("(w)(ww)",s)
print(res.group())#输出的是匹配到的全字符
#group(0)的作用等同于group()，就是匹配出来的全规则，group(1)是第一个括号的内容，group(2)是第二个括号的内容
print(res.group(0),res.group(1),res.group(2))

# 下面的用法是错的，不可以跨字符使用
# res = re.match("(w)(ww)(co)",s)

s1 = "hellolemonfixlemon"

# -------------findall函数:
# 作用：是循环匹配字符串
# 规则：从字符串的头部开始匹配
# 用法：match("匹配规则",目标字符串)
# 返回数据类型：列表，将在字符串中，所有根据匹配规则匹配到的字符串存放入列表中
res = re.findall("l",s1)
print(res)

# -------------findall函数:
# 如果匹配规则中有分组,那么输出的结果是列表嵌套元祖
res = re.findall("(le)(mon)",s1)
print(res)


class DoRegx:
    @staticmethod
    def do_regx():
        d={"normal_tel":"123","pwd":"7777"}
        s = "{'mobilephone':'${normal_tel}','pwd':'${pwd}'}"
        # 思想是，首先声明两个字典a,b
        # a字典中的变量值（value），为另外一个字典的key，
        # 然后将a字典中的变量值根据正则匹配取出来， 并且作为获取b字典value的key值
        # 然后将a字典对应key的value值更换为取到的对应b字典key的value值
        while re.search('\$\{(.*?)\}',s):
            res = re.search('\$\{(.*?)\}',s)
            key = res.group()
            value = res.group(1)
            print(res)
            print(res.group())
            print(res.group(1))
            s = s.replace(key,d[value])
        print(s)
        return s

if __name__ == '__main__':
    DoRegx.do_regx()


