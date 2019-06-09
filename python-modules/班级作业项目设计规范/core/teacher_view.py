# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 12:25
# @Author  : jesse
# @File    : teacher_view.py

import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from common import education
from db import db_data
from common import choise

#选择班级
def choose_grade():
    # 选择一个老师
    get_teacher_obj = choise.Choise_Teacher()

    # 选择一个班级
    get_grade_obj = choise.Choise_Grade()

    #老师关联班级
    get_teacher_obj.choose_classes(get_grade_obj)

    #更新数据
    db_data.update(get_teacher_obj,"teachers")
    db_data.update(get_grade_obj, "grades")

#查看学生
def show_students():
    # 选择一个老师
    get_teacher_obj = choise.Choise_Teacher()

    #打印该老师下的学生信息
    get_teacher_obj.show_students()

#修改成绩

def modify_score():
    # 选择一个老师
    get_teacher_obj = choise.Choise_Teacher()

    # 选择学生
    get_student_obj = choise.Choise_Student()

    #输入分数:
    score = input("请为该名学生打分:")
    if not score.isdigit() or int(score) < 0 or int(score) > 100:
        print("输入分数不正确")
        return

    #调用teacher类下的修改分数方法
    get_teacher_obj.modify_score(get_student_obj,score)
    print("%s 学生打分成功" %get_student_obj.name)

    #更新数据
    db_data.update(get_student_obj,'students')
    db_data.update(get_teacher_obj,'teachers')
    db_data.update(get_teacher_obj, 'teachers')
    print("%s 的成绩修改为: %s" % (get_student_obj.name, db_data.get_info(get_student_obj.name).score))

#查看教师
def show_teacher():
    # 选择一个老师
    get_teacher_obj = choise.Choise_Teacher()

    get_teacher_obj.show_info()

def run():
    print("教师视图：")
    print("=" * 20)
    while True:
        print("1.选择班级\n2.查看学生\n3.修改成绩\n4.查看教师\n"
              "0.退出")
        res = input("输入序号：")

        if res == "1":
            choose_grade()
        elif res == "2":
            show_students()
        elif res == "3":
            modify_score()
        elif res == "4":
            show_teacher()
        elif res == "0":
            print("退出成功！")
            break
        else:
            print("请选择正确的编号")


if __name__ == "__main__":
    run()