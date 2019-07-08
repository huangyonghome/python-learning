# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 12:25
# @Author  : jesse
# @File    : student_view.py

import os
import sys

# 导入路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

from common import education
from db import db_data
from common import choise

#添加学生
def add_student():
    student_name = input("请输入学生姓名:")
    #选择学校
    get_school_obj = choise.Choise_School()

    #请选择班级
    get_grade_obj = choise.Choise_Grade()

    student = education.Student(student_name, get_school_obj, get_grade_obj)
    db_data.update(student,"students")
    db_data.update(get_school_obj,"schools")
    db_data.update(get_grade_obj,"grades")

#交学费
def pay_tuition():

    #选择学生
    get_student_obj = choise.Choise_Student()

    #输入学费金额
    tuition = input("请输入学费:")
    if not tuition.isdigit():
        print("输入金额不正确")
        return

    #调用student实例方法
    get_student_obj.pay_tuition(int(tuition))

    #更新数据
    db_data.update_student(get_student_obj)

#选择班级
def choose_grade():

    # 选择学生
    get_student_obj = choise.Choise_Student()
    #选择班级
    get_grade_obj = choise.Choise_Grade()

    #选择一个班级
    get_student_obj.choose_classes(get_grade_obj)

    ##更新班级和学生实例信息
    db_data.update(get_grade_obj,"grades")
    db_data.update(get_student_obj, "students")

#选择学校

def choose_school():
    # 选择学生
    get_student_obj = choise.Choise_Student()
    # 选择学校名
    get_school_obj = choise.Choise_School()

    #选择一个学校
    get_student_obj.choose_school(get_school_obj)

    #更新学校和学生实例信息
    db_data.update(get_student_obj,"students")
    db_data.update(get_school_obj,"schools")


#查看学生

def show_students():
    db_data.print_infos("students")


#查看学生详细信息
def show_student():
    # 选择学生
    get_student_obj = choise.Choise_Student()

    #调用student实例的show_info方法打印详细信息
    get_student_obj.show_info()


def run():
    print("学生视图：")
    print("=" * 20)
    while True:
        print("1.增加学生\n2.交学费\n3.选择班级\n4.选择学校\n"
              "5.查看学生\n6.查看详细\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            add_student()
        elif res == "2":
            pay_tuition()
        elif res == "3":
            choose_grade()
        elif res == "4":
            choose_school()
        elif res == "5":
            show_students()
        elif res == "6":
            show_student()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")


if __name__ == "__main__":
    run()