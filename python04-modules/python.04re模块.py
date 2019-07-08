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
str1 = 'alex,jerry;jesse|lyon wusir'

#re可以将不规则的分隔符进行切分.而字符串的split方法做不到这点
# print(re.split(" |,|;|\|",str1))

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
# print(re.findall(r'666\Z','hello jesse \n666',flags=re.M))



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
# res1 = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242")
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

# str1 = "company companies compan comp companiessss"
#
# print(re.findall("compan(y|ies)",str1))
#
# print(re.findall("company|companies",str1))




'''
分组匹配:
分组就是用一对圆括号“()”括起来的正则表达式，匹配出的内容就表示一个分组.用match方法
可以匹配一个分组,然后用group()来取出分组匹配到的内容.
分组匹配类似于shell里的sed分组()匹配.
注意:正则表达式有一个隐含的全局分组0

'''
# str1 = '010-12345'
# r = re.compile('(\d{3})-(\d{5})')
# res = re.match(r,str1)
#
# print(res.group(0))  #打印全局匹配到的字符串
# print(res.group(1))  #打印第一个分组(\d{3})匹配到的字符串
# print(res.group(2))  #打印第二个分组(\d{5})匹配到的字符串
# print(res.groups())  #元祖形式返回分组1和2
#
#
# str3 = '<script src="https://ss1.bdstatic.com/"'
#
# #这里采用分组匹配,匹配到的是https://ss1.bdstatic.com/ URL地址
# print(re.findall('src=(".*?")',str3))
# res = re.match('<script src=(".*?")',str3) #注意match方法是从起始位置开始匹配.所以直接写src=(".*?")是匹配不到的
# print(res.group(1))

'''
贪婪模式: 默认的匹配方式,意思是尽可能多的匹配字符
'''

# s = "this is a number 234-235-22-423"
#
# r = re.match(".+(\d+-\d+-\d+-\d+)",s)
# print(r.group(1))



'''
非贪婪模式: 总是尝试匹配尽可能少的字符。
在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
此时的```?```不再表示匹配前一个字符0次或者多次的意思,而是作为限制符.
意思就是只要匹配到,就取出.
'''

#
# s = "this is a number 234-235-22-423"
#
# r = re.match(".+(\d+-\d+-\d+-\d+)",s)
# print(r.group(1))

# str1 = "a1b atb aTb a3b a1b a-b a%b a!b a9b aYb a&b"
#

'''
练习题
'''
# #取出中间为特殊字符
# print(re.findall('a[%!\-&]b',str1))
#
# #取出中间为数字的
# print(re.findall('a[0-9]b',str1))
# print(re.findall('a[\d]b',str1))
#
# #取出中间为小数字母的
# print(re.findall('a[a-z]b',str1))
#
# #取出中间为大写字母的的
# print(re.findall('a[A-Z]b',str1))
#
# #取出字母或者数字的
# print(re.findall('a[\w]b',str1))
#
# #取出中间不为数字的
# print(re.findall('a[\D]b',str1))
# print(re.findall('a[^0-9]b',str1))


str2 = "1-2*(60+(-40.35/5)-(-4*3))"
#
# # 1.1 匹配所有的整数
#
print(re.findall('[^\.?\d+](\d+)',str2))
# print(re.findall('\d+',str2))
#
# # 1.2 匹配所有的数字（包含小数）
# print(re.findall(r'\d+\.?\d*|\d*\.?\d+',str2))
#
# # 1.3 匹配所有的数字（包含小数包含负号）
#
# print(re.findall('\-?\d*\.?\d+',str2))


#找出下面的p标签
s1 = '''
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7459977.html" target="_blank">python基础一</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7562422.html" target="_blank">python基础二</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/9439483.html" target="_blank">Python最详细，最深入的代码块小数据池剖析</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7738630.html" target="_blank">python集合,深浅copy</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8183203.html" target="_blank">python文件操作</a></p>
<h4 style="background-color: #f08080;">python函数部分</h4>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8241942.html" target="_blank">python函数初识</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8259929.html" target="_blank">python函数进阶</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8305011.html" target="_blank">python装饰器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423526.html" target="_blank">python迭代器,生成器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423937.html" target="_blank">python内置函数,匿名函数</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8743408.html" target="_blank">python递归函数</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/8743595.html" target="_blank">python二分查找算法</a></p>

'''

# print(re.findall(r'^<p>(.*)</p>$',s1,flags=re.M))

#找出下面的p标签包含的URL

# print(re.findall(r'^<p>.*?href="(.*?)".*</p>$',s1,flags=re.M))