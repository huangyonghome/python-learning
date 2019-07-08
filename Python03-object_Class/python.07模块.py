# -*- coding: utf-8 -*-
# @Time    : 2019-06-07 10:52
# @Author  : jesse
# @File    : python.07模块.py

#序列化模块

import json

dic = {'name':'jesse','age':25,"sex":"male"}
# print(dic)
#
# ret = json.dumps(dic)
#
# print(ret,type(ret))
#
# response = json.loads(ret)
#
# print(response,type(response))



# dic = {'name':'jesse','age':25,"sex":"male"}
#
# ret = json.dumps(dic)
#
# response = json.loads(ret)
#
# print(response,type(response))
#
# # with open('dic.json','w+') as f:
# #     f.write(json.dumps(dic))
#
# file = open('dic.json','r')
# print(file.read())
# file.close()

#多文件存储

# dic1 = {'name':'jesse'}
# dic2 = {'name':'jerry'}
# dic3 = {'name':'Lyon'}
#
# with open('dic1.json','w+') as f:
#     f.write(json.dumps(dic1)+'\n')
#     f.write(json.dumps(dic2)+'\n')
#     f.write(json.dumps(dic3)+'\n')
#
#
# f1 = open('dic1.json','r')
# print(f1.read())
# for line in f1:
#     print(json.loads(line))
# f1.close()


#pickle模块

# import pickle
# dic = {'name':'jesse','age':25,"sex":"male"}
#
# f = open('dic.pickle','wb')
# pickle.dump(dic,f)
# f.close()
#
# # str_dic = pickle.dumps(dic)
# # print(str_dic)
# #
# # dic2 = pickle.loads(str_dic)
# # print(dic2)
#
# f1 = open('dic.pickle','rb')
# print(pickle.load(f1))

#常见模块

import random
# print(random.random()) #0-1之间的浮点数
# print(random.uniform(0,10)) #0-10之间的浮点数
# print(random.randint(0,10)) #0-10之间的整数
# print(random.randrange(1,10,2)) #1-10之前的奇数,
# print(random.choice('1,2,3,4,5')) #随机选择一个,注意符号也在内
# print(random.sample([1,2,3,4,5],3)) #随机选3个元素生成一个列表
#
# l1 = [1,2,3,4,5]
# random.shuffle(l1) #随机打乱次序,修改原有对象
# print(l1)
#
# s1 = 'jesse'
# random.shuffle(s1) #不支持字符串方法
# print(s1)


#练习题: 生成一个随机的6位数的验证码.包括数字和字母

# def auth_code():
#     res = ''
#     for i in range(6):
#         num = str(random.randint(0,9))
#         #用char方法可以将97-122的ascii码表示字母a-z.
#         alp = chr(random.randint(97,122))
#         code = random.choice([num,alp])
#         res += code
#     return res
#
# print(auth_code())

import json

path = 'dic2.json'

def dump(obj):
    f = open(path,"w")
    json.dump(obj,f)
    f.close()

def load():
    f = open(path,"r")
    info = json.load(f)
    f.close()
    return info

def get_info():
    info = load()
    print(info)
    for k,v in info.items():
        print(k,v)

def update(k,v):
    # obj = load()
    # obj.update(dct)
    # dump(obj)
    obj = load()
    obj[k] = v
    dump(obj)


#写入文件
res = dump(dic)

#查询文件
get_info()

#更新值

update('name','Lyon')
get_info() #再次查询

