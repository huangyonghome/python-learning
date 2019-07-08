# -*- coding: utf-8 -*-
# @Time    : 2019-06-09 10:10
# @Author  : jesse
# @File    : choise.py


import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from common import education
from db import db_data
from core import school_view,student_view,teacher_view

#选择一个学校通用函数..下面其他函数的功能和此大同小异,所以后续其他函数参考下面的注释信息
def Choise_School():
    #接收目前学校名信息.这是一个列表类型
    info_list = db_data.print_infos('schools')

    #如果目前还没有添加任何学校,则手动创建一个
    if info_list == None:
        choose = input("是否需要新增一个学校?(yes or no):")

        if choose == 'yes' or choose == "y":
            get_school_obj = school_view.add_school()

        else:
            print("选择错误")
            exit(1)

    else:
        #选择学校名对应的序号
        num = input("选择学校序号：")
        #判断输入合法性
        if not num.isdigit() or int(num) < 0 or int(num) > len(info_list) - 1:
            print("选择错误")
            exit(1)
        else:
            #获取学校名
            school_name = info_list[int(num)]
            #获取学校名对应的学校实例对象
            get_school_obj = db_data.get_infos('schools').get(school_name)

    #返回学校实例对象
    return get_school_obj

def Choise_Grade():
    info_list = db_data.print_infos("grades")
    if info_list == None:
        choose = input("是否需要新增一个班级?(yes or no):")

        if choose == 'yes' or choose == "y":
            get_grade_obj = school_view.add_grade()


        else:
            print("选择错误")
            exit(1)
    else:
        num = input("选择班级序号：")
        if not num.isdigit() or int(num) < 0 or int(num) > len(info_list)-1:
            print("选择错误")
            exit(1)

        else:
            grade_name = info_list[int(num)]
            get_grade_obj = db_data.get_infos('grades').get(grade_name)
    return get_grade_obj


def Choise_Teacher():
    info_list = db_data.print_infos("teachers")
    if info_list == None:
        choose = input("是否需要新增一个老师?(yes or no):")

        if choose == 'yes' or choose == "y":
            get_teacher_obj = school_view.add_teacher()


        else:
            print("选择错误")
            exit(1)

    else:
        num = input("选择老师序号：")
        if not num.isdigit() or int(num) < 0 or int(num) > len(info_list) - 1:
            print("选择错误")
            exit(1)

        else:
            teacher_name = info_list[int(num)]
            get_teacher_obj = db_data.get_infos('teachers').get(teacher_name)
    return get_teacher_obj


def Choise_Course():
    info_list = db_data.print_infos("courses")
    if info_list == None:
        choose = input("是否需要新增一个课程?(yes or no):")

        if choose == 'yes' or choose == "y":
            get_course_obj = school_view.add_course()


        else:
            print("选择错误")
            exit(1)

    else:
        num = input("选择老师序号：")
        if not num.isdigit() or int(num) < 0 or int(num) > len(info_list) - 1:
            print("选择错误")
            exit(1)

        else:
            courses_name = info_list[int(num)]
            get_course_obj = db_data.get_infos('courses').get(courses_name)
    return get_course_obj


def Choise_Student():
    print("选择学生：")
    info_list = db_data.print_infos("students")
    if info_list == None:
        choose = input("是否需要新增一个学生?(yes or no):")

        if choose == 'yes' or choose == "y":
            get_student_obj = student_view.add_student()


        else:
            print("选择错误")
            exit(1)

    else:
        num = input("选择老师序号：")
        if not num.isdigit() or int(num) < 0 or int(num) > len(info_list) - 1:
            print("选择错误")
            exit(1)

        else:
            student_name = info_list[int(num)]
            get_student_obj = db_data.get_infos('students').get(student_name)
    return get_student_obj