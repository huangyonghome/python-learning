# -*- coding: utf-8 -*-
# @Time    : 2019-04-18 16:38
# @Author  : jesse
# @File    : 格式化输出.py


# name = input('请输入姓名:')
# age = input('请输入年龄:')
# job = input('请输入工作:')
# hobbies = input('请输入爱好:')

#
# msg = """
#
# --------- info of %s --------------
# name:     %s
# age:      %d
# job:      %s
# hobbies:  %s
# ----------------------------------
# """ % (name,name,int(age),job,hobbies)
#
#
# print(msg)


#第二种字典格式化方法

# dic = {'name': name, 'age': int(age), 'job': job, 'hobbies': hobbies}
#
#
# msg = """
#
# --------- info of %(name)s --------------
# name:     %(name)s
# age:      %(age)d
# job:      %(job)s
# hobbies:  %(hobbies)s
# ----------------------------------
# """ % dic
#
#
# print(msg)
# a=(85-72)%72
# print('小明的成绩提高了 %.1f %%' %a)
#
# b=((85/72)-1)*100
# print(b)
# print('小明的成绩提高了 %.1f %%' %b)

#print((85-72)/72)


# b=((85/72)-1)*100
#
# print('小明的成绩提高了 %.1f %%' %b)
#
#
# print(2/4)

a = 1/3
print(a)
print(type(a))