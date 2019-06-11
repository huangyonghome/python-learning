# -*- coding: utf-8 -*-
# @Time    : 2019-06-11 22:06
# @Author  : jesse
# @File    : python.04re模块.py

import re

#re.match模块 格式 (*pattern*, *string*, *flags=0*) :
#
# 匹配成功,则返回<class '_sre.SRE_Match'>类型.用group()方法可以取出结果.否则返回None

# res = re.match('lyon','jesse')
#
# print(type(res))
#
# print(res.group())

#re.search 格式 (*pattern*, *string*, *flags=0*) :和re.match一样.


# res = re.search('\d+','abc123') # \d匹配数字
# print(type(res))
# print(res.group())

# re.findall (*pattern*, *string*, *flags=0*) :  👈

#匹配字符串所有的内容，把匹配到的字符串以列表的形式返回

# res = re.findall("\d+","123acb3223") #返回['123','3223']
# res1 = re.findall("\d","123acb3223") #返回['1','2','3'.....]
#
# print(res,res1)

#re.split (*pattern*, *string*, *maxsplit=0*, *flags=0*) :  👈

#指定格式进行切分，返回一个列表

# res = re.split("\d+","abc123xyz456-=79")
# print(res)

#re.sub (*pattern*, *repl*, *string*, *count=0*, *flags=0*) : 👈

#替换匹配到的字符串并返回替换后的结果

# res = re.sub("abc","xyz","abc123abc456") #用abc匹配"abc123abc456",匹配到的用xyz替换abc
#
# print(res)
#
# res1 = re.sub("abc","xyz","abc123abc456",count=1) #只匹配一次
# print(res1)


'''
flags:


标志	说明
re.I (re.IGNORECASE)	忽略大小写（括号内为全拼写法，效果一样）
re.M (MULTILINE)	多行模式，改变 '^' 和 '$' 的行为 （改变？见下节匹配模式）
re.S (DOTALL)	任意匹配模式，改变 ' . ' 的行为（同上）
re.L (LOCALE)	做本地化识别（locale-aware）匹配，法语等
re.X (VERBOSE)	该标志通过给予更灵活的格式以便将正则表达式写得更易于理解
re.U	根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B

'''

# #忽略大小写
#
# res =re.findall("a","abcAbc",flags=re.I)
# print(res)
#
# #多行模式
#
# res1 = re.search(r"^a","\nabc\neee") #匹配不到a,因为a被换行了
# res2 = re.search(r"^a","\nabc\neee",flags=re.M) #可以匹配到a
# print(res2.group())


# \A 只从开头进行匹配
# res = re.search("\Aabc","alexabc") #匹配不到abc,因为不是abc字母开头
# print(res)


# | 或匹配

# res = re.search("(abc)|(ABC)","ABCabcCD") #匹配到第一个ABC,返回
#
# print(res.group())
#
# print(re.findall("abc|ABC","ABCabcCD")) #匹配到所有,也就是ABC,abc

#(?P<>) 命名分组匹配

# res = re.search("(?P<城市>\d{4})(?P<街道>\d{4})(?P<楼牌号>\d{2})","12345678903443")
#
res1 = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242")
print(res1)
# # print(res)
#
# print(res.groupdict("城市"))
# print(res1.groupdict())

#re.compile 生成一个匹配对象,以便多次调用

r1 = re.compile("abc\d")

# res = re.search(r1,"abc123abc456")
# print(res.group())
#
# res1 = re.search(r1,"abc345abcd")
# print(res1.group())

#完整匹配 re.fullmatch(pattern, string, flags=0) :

# res = re.fullmatch(r1,'abc12') #匹配失败不是完全匹配,多了个数字2
# print(res)


# source ='192.168.0.1 25/Oct/2012:14:46:34 "GET /api HTTP/1.1" 200 44 "http://abc.com/search" "Mozilla/5.0"'
#
# res = re.match('^(?P<remote_ip>[^ ]*) (?P<date>[^ ]*) '
#                 '"(?P<request>[^"]*)" (?P<status>[^ ]*) (?P<size>[^ ]*) '
#                 '"(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"',source)
#
# res = res.groupdict()
# for k in res:
#     print(k+": "+res[k])
#
