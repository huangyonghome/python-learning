#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 上午10:31
# @Author  : jesse
# @File    : python字符串.py

#字符串是不可变的,任何修改字符串的行为都等于是生成了一个新的字符串.

### 1.拼接

#有两个方法,一是用+号,例如:

a = 'hello'
b = 'jesse'

# print(a+b)

#第二个方法是用Join方法,例如
# print(a.join(b)) #jhello  ehello shello shello .... 用a将字符串b的每个元素进行拼接
#
# print("".join(b))
#
# print(",".join(b))

###2.查找

#### index方法
b = 'jesse'
# print(b.index('e')) #只返回匹配到的第一个元素
# print(b.index('a')) #匹配不到则会报错

#### find方法
# print(b.find('e'))
# #和index区别是,find如果没有找到匹配的字符,会返回-1
# print(b.find('a'))
#
# #当然,两者都支持定义起始位置,即从某个起始位置开始查找.
#
# # print(b.find('e',2)) #从第二个位置开始查找
# # print(b.find('e',2,3)) #从第二个位置开始查找,但是只查找到第三个结束,所以没有找到e字符串
#
# print(b.index('e',2)) #从第二个位置开始查找
# print(b.index('e',2,3)) #从第二个位置开始查找,但是只查找到第三个结束,所以没有找到e字符串

#### 3.统计
# count表示统计某个元素的个数
# print(b.count('e'))
#
# #len表示字符串的长度
# print(len(b))

#### 4.切片
#切片就是通过索引（索引：索引：步长）截取字符串的一段，形成新的字符串（原则就是顾头不顾腚).

b = 'jesse'
# print(b[0:3]) #从第0个下标开始截取到第3个..如果起始位置为0.则0可以不用写
# #等同于
# print(b[:3])

#如果是全部截取,则不需要加起始值和截止值
# print(b[:])

# print(b[-1:]) #输出最后一个字符
# print(b[-1:-3:-1]) #输出最后一个字符到倒数第三个字符,注意这里要用-1表示步长,因为是倒序匹配,所以步长也是倒序
#
# print(b[::-1]) #倒序打印,也就是字符串翻转

#步长表示每隔多少个间隔截取字符串
# print(b[::-2])

#### 4.检测
b = 'jesse'
#
# print('s' in b)
# print(b.isalpha())
#
# print(b.isdigit())

# print(b.startswith('j'))
# print(b.endswith('e'))

#### 5.大小写

# print(b.swapcase())
# print(b.capitalize())
# print(b.upper())
# print(b.lower())

#### 6.split()

# b = 'jeese hello world'
# print(b.split())
#
# b = '/usr/bin:/usr/sbin:/usr/local/bin:/bin:/sbin'
# print(b.split(':'))


#### 7.strip()
# b= '    jesse     '
# print(b.strip())
#
# print(b.lstrip())
# print(b.rstrip())

#### 8.replace()
# b = 'jesse'
# print(b.replace('s','a'))