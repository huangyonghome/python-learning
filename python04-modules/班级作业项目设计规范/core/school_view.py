# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 22:00
# @Author  : jesse
# @File    : school_view.py

import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from common import education
from db import db_data
from common import choise


def add_school():
    school_name = input("请输入学校名:").strip()
    school_city = input("请输入学校地址:").strip()
    school = education.School(school_name, school_city)

    db_data.update(school,'schools')
    return school


def add_teacher():
    teacher_name = input("请输入老师名:").strip()

    #选择学校
    get_school_obj = choise.Choise_School()

    #通过学校实例创建老师
    teacher = get_school_obj.create_teacher(teacher_name)

    #更新老师和学校信息
    db_data.update(teacher,"teachers")
    db_data.update(get_school_obj,"schools")
    print("老师 %s 创建成功！"% teacher.name)
    return teacher


def add_course():
    print("请填写课程信息：")
    course_name = input("名称：")
    cycle = input("周期：")
    price = input("学费：")
    #选择学校
    get_school_obj = choise.Choise_School()

    course = get_school_obj.create_course(course_name, cycle, price)
    db_data.update(course,"courses")
    db_data.update(get_school_obj,"schools")
    return course


def add_grade():
    grade_name = input("请输入班级名:")
    # 选择学校
    get_school_obj = choise.Choise_School()

    #选择一个老师
    get_teacher_obj = choise.Choise_Teacher()

    #选择课程:
    get_course_obj = choise.Choise_Course()

    #更新数据
    grade = get_school_obj.create_class(grade_name, get_teacher_obj, get_course_obj)
    db_data.update(grade,"grades")
    db_data.update(get_school_obj,"schools")
    return grade


#查看学校信息
def show_schools():
    db_data.print_infos("schools")

#查看老师信息

def show_teachers():
    db_data.print_infos("teachers")


#查看课程信息
def show_courses():
    db_data.print_infos("courses")

#查看班级信息
def show_grades():
    db_data.print_infos("grades")

#查看教师详细信息

def show_teacher():
    # 选择一个老师
    get_teacher_obj = choise.Choise_Teacher()

    print("teacher:name: %s\t school:%s\t grade:%s" %(get_teacher_obj.name, get_teacher_obj.school, get_teacher_obj.classes))

#查看学校详细信息

def show_school_detail():
    # 选择学校
    get_school_obj = choise.Choise_School()
    get_school_obj.show_info()


def run():
    print("学校视图：")
    print("=" * 20)
    while True:
        print("1.增加学校\n2.增加老师\n3.增加课程\n4.增加班级\n"
              "5.查看学校\n6.查看老师\n7.查看课程\n8.查看班级\n"
              "9.查看教师详细\n10.查看学校详细信息\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            add_school()
        elif res == "2":
            add_teacher()
        elif res == "3":
            add_course()
        elif res == "4":
            add_grade()
        elif res == "5":
            show_schools()
        elif res == "6":
            show_teachers()
        elif res == "7":
            show_courses()
        elif res == "8":
            show_grades()
        elif res == "9":
            show_teacher()
        elif res == "10":
            show_school_detail()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")

if __name__ == "__main__":
    run()