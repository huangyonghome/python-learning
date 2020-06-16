# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 12:45
# @Author  : jesse
# @File    : db_data.py


import os,sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)
import pickle

from conf import settings

#存储数据
def  dump(obj):
    f = open(settings.path, "wb")
    pickle.dump(obj,f)
    # json.dump(obj,f)  #抛弃了json方法,是因为Json不能存储实例对象
    f.close()


#加载数据
def load():
    f=  open(settings.path, "rb")
    info = pickle.load(f)
    f.close()
    return info

#打印数据

# 打印所有数据信息
def print_all_infos():
    infos = load()
    print("=" * 50)
    print(infos)
    for key in infos:
        print(key,":")
        for key2 in infos.get(key):
            print("\t",key2, ":", infos.get(key).get(key2))
    print("=" * 50)

#打印学校或者课程等一类的数据信息
def print_infos(key):
    list_info = [] #临时列表,存储传入的参数的名字,例如学校名,课程名,老师名等
    infos = load()
    print(key.center(50, "="))
    #如果当前没有任何学校,老师,课程等等相关信息,则返回None
    if not infos.get(key) :
        print("当前还没有任何信息")
        return None
    #通过enumerate方法为键名添加对应的序列号
    for i,key2 in enumerate(infos.get(key)):
        #将键名添加进临时列表
        list_info.append(key2)
        print("\t",i,"\t",key2)
    print("=" * 50)
    return list_info #返回列表


#查询数据
def get_infos(variety): #接收要查询的信息.比如是查询school还是teacher等等
    infos = load()
    return infos.get(variety) #获取嵌套的子字典的键名.也就是学校名,老师名等


#追加数据

def update(obj,variety): #更新数据
    current = load()
    current[variety].update({obj.name:obj}) #字典格式:名字:实例化对象
    dump(current)



def init():
    # 存储结构：
    infos = {
        "schools": {
            # "school_name": "school_obj"
        },
        "teachers": {
            # "teacher_name": "teacher_obj"
        },
        "students": {
            # "student_name": "student_obj"
        },
        "grades": {
            # "grade_name": "grade_obj"
        },
        "courses": {
            # "course_name": "course_obj"
        }
    }
    # 初始化数据
    res = input("是否初始化数据？（y）:")
    if res == "y":
        dump(infos)
        print("数据初始化成功！")
    else:
        print("数据初始化失败！")

if __name__ == '__main__':
    init()
    # print_infos('schools')