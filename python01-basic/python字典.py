#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 下午7:00
# @Author  : jesse
# @File    : python字典.py

#1.创建一个空字典

# dic = dict()
#或者
# dic1 = {}
#
# print(dic)
# print(dic1)

#创建字典
dic = {"name":"jesse","age":33,"job":"it","sex":"male"}

# dic.update({"name":"jerry"})
#
# print(dic)


#### 2.增加键值对

#给字典增加一个新的键值对.如果键不存在,则添加
#
# dic['company'] = 'dwd'
#
# print(dic)

#如果字典已经存在了这个键.则用新的值替代
#
# dic['company'] = 'hsq'
#
# print(dic)

#通过setdefault方法也可以增加一个值
# dic.setdefault('school',"college")
#
# print(dic)

#和刚才相反.如果键已经存在,则新值不会生效.
# dic.setdefault('school','primary')

# print(dic)

'''
3.修改字典值
'''

# dic['name'] = 'jessehuang'
# print(dic)

#update方法也可以修改字典键值对.如果键已经存在,则修改值,如果不存在,则添加
# dic.update({"name":"Lyon","company":"internet"})

'''
4.删除一个字典的键值对'''

#1.pop删除法

# dic.pop('name')
# print(dic)
# 注意pop方法有返回值
# print(dic.pop('name'))

#2.del删除法
# del dic['name']
# print(dic)

# 3.随机删除

# dic.popitem()
# print(dic)
# dic.popitem()
# print(dic)

'''
查找
'''
#查找键是否存在于字典中

# print('name' in dic)
# print('jesse' in dic)

#2.获取键的值
# print(dic['jesse'])

# get方法优雅的获取字典中某个键的值
# print(dic.get('name'))

#如果没有这个键,则返回none
# print(dic.get('jesse'))

'''
遍历
'''

# for key in dic:
#     print(key,dic[key])

# for i in dic:
#     print(i)

# for k,v in dic.items():
#     print(k,v)

'''
字典嵌套
'''
dics = {
    'name':{
        'jesse':{
            'age':22,
            'job':'it',
            'sex':'male'
        },
        'jerry':{
            'age':23,
            'job':'it',
            'sex':'female'
        },

    },
    'home': {
        'jesse':{
            'live':'shanghai',
            'hometown':'jiangxi'
        },
        'jerry':{
            'live':'beijing',
            'hometown':'wuhan'
        }
    },
    'company':{
        'jesse':{
            'name':'dwd',
            'industry': 'internet'
        },
        'jerry':{
            'name': 'bat',
            'industry': 'internet'
        }
    }
}
#
dics['name']['jesse']['age'] = 33
print(dics['name']['jesse'])
# #
# # dict
#
# #练习
#
# print(dic)
#
# dic['name'] = 'new'
#
# print(dic)
#
# dic.setdefault('name','jesse')
#
# print(dic)
#
# dic.setdefault('school','college')
#
# print(dic)
#
# dic.pop('school')
#
# print(dic)
#
# del dic['name']
#
# print(dic)
#
# print(dic.get('school'))
#
# print(dic)
#
# for k,v in dic.items():
#     print(k,v)
#
# print(dic.items())
#
#
# l1 = ['a','b','c','d']
#
# dic1 = dict.fromkeys(l1,'default')
#
# print(dic1)
#
#
# print(dic.keys())


#作业


#1.将下列字典中的key键含有'k'元素的所有键值对删除

#下面的方法报错..."RuntimeError: dictionary changed size during iteration"
#注意,字典在循环或者迭代的时候,不能修改该字典的内容.
#
# dic = {'k1':'v1',"k2":'v2',"k3":'v3','name':'jesse'}
#
# for k in dic:
#     if 'k' in k:
#         del dic[k]
#
# print(dic)
#
# #但是可以在循环一个列表的时候修改该字典
#
# #新建一个空列表
# l1 = []
#
# #循环列表,将满足要求的key键添加进一个列表
# for k in dic:
#     if 'k' in k:
#         l1.append(k)
#
# #循环列表,这里就是循环字典的KEY..然后删除dic的键
# for keys in l1:
#     del dic[keys]
#
# print(dic)


# dic1 = {1:{'name':'jesse',"age":22},2:{"name":"jerry","age":23}}
#
# print(dic1[1])
#
#
# print(dic1.keys())
#
# dic = {"name":"jesse","age":33,"job":"it","sex":"male"}
# # print('name' in dic)
#
#
# for i,k in (enumerate(dic)):
#     print(i,"\t",k)

# choise = int(input(">>>"))
# print(dic.index)

# a = dic.get("name1") or "haha"
#
# print(a)

# dic = {}
# l1 = []
# for i in range(2):
#     dic["name"] = 'jesse' + str(i)
#     dic["age"] = i
#     print(dic)
#     l1.append(dic)
#     print(l1)
#
# print(l1)
#

