# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 12:22
# @Author  : jesse
# @File    : start.py



'''
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校，
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程
'''


import sys,os


BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from core import student_view
from core import teacher_view
from core import school_view

def main():
    choice = input("请选择角色：0.学校，1.教师，2.学生")
    if choice == "0":
        school_view.run()
    elif choice == "1":
        teacher_view.run()
    elif choice == "2":
        student_view.run()
    else:
        print("角色选择失败")

if __name__ == "__main__":
    main()