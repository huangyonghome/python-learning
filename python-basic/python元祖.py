#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 下午12:49
# @Author  : jesse
# @File    : python元祖.py

#定义一个元祖

name = ('jesse','Lyon','tony','david')

#如果元祖只有一个元素，则要加个逗号，表示这个是个元祖

name1 = ('jesse',)

# print(name,name1)

#元祖也支持索引，切片。所以访问方式和列表一样

# print(name[0])
#
# print(name[:3])
## 元祖不能修改。所以下面这个操作是非法的

# name[0]='jessehuagn'

#但是可以复制，修改成一个新元祖

# name2 = name + name1
# print(name2)
#
# name2 = name * 2
# print(name2)

'''
元祖可以被整个删除,但是不能删除元祖的元素
'''

#del name
# print(name)
# del name[0]

'''
切片
'''
# print(name[0])
# print(name[:3])

'''
检测
'''
# print('jesse' in name )

'''
将列表转换为元祖
'''

l1 = ['jesse','huang',123]

print(tuple(l1))