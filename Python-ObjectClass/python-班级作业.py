#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 下午9:31
# @Author  : jesse
# @File    : python-班级作业.py

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

class School:
    def __init__(self,name,city):
        self.name = name
        self.city = city
        self.classes = []
        self.course = []
        self.student = []
        self.teacher = []

    # def create_class(self,class_name):
    #     print("creating a class")
    #     self.classes.append(class_name)
    #
    # def create_course(self,course_name):
    #     print("creating a course")
    #     self.course.append(course_name)

class Classes:
    def __init__(self,school,name):
        self.school_name = school.name
        self.name = name
        school.classes.append(name)
        self.course = []
        self.teacher = []
        self.student = []


class Course:
    def __init__(self,school,classes,name,price,period):
        self.school_name = school.name
        self.name = name
        self.price = price
        self.period = period
        school.course.append(name)
        classes.course.append(name)

\
class Teacher:
    def __init__(self,school,name):
        self.school_name = school.name
        self.name = name
        school.teacher.append(name)


    def Choose_class(self,classes):
        self.class_name = classes.name
        classes.teacher.append(self.class_name)

    def Get_class_student(self,classes):
        self.class_name = classes.name
        print("HI,dear teacher %s ,你班级学员列表如下:" %self.name)
        print(classes.student)

    def Change_score(self,student):
        student_course = list(student.score.keys())
        print("The student {} has several courses: {} ".format(student.name,student_course))
        grade = input("please choose a course to grade:")
        if grade not in student_course:
            print("{} doesn't exist".format(grade))
            exit(1)

        score_number = input("please input a new score:")
        if score_number.isdigit():
            student.score[grade] = score_number
            print("Student %s's score is:" %student.name)
            print(student.score)
        else:
            print("{} is not a valid number".format(score_number))
            exit(1)


class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sed = sex
        self.score = {}

    def Enroll(self,school):
        '''注册一个学校'''
        self.school_name = school.name
        school.student.append(self.school_name)

    def Choose_Class(self,classes):
        '''选择一个班级'''
        self.class_name = classes.name
        classes.student.append(self.name)
        print("HI, dear {},you are belonged class:{} ".format(self.name,self.class_name))
        print("the classe has below courses:",classes.course)
        for course_name in classes.course:
            self.score[course_name] = 0

    def Pay_tuition(self,tuition):
        '''交学费'''
        print("您已经缴纳了%d学费" %tuition)


#创建学校
school_SH = School('oldboy_sh','shanghai')
school_BJ = School('oldboy_bj','beijing')

#创建班级
class_201903 = Classes(school_SH,'201903')
class_201904 = Classes(school_BJ,'201904')

#创建课程
linux = Course(school_BJ,class_201904,'linux',6000,90)
go = Course(school_SH,class_201903,'go',15000,100)
py = Course(school_BJ,class_201904,'python',10000,120)

#创建讲师
alex = Teacher(school_BJ,'alex')
wusir = Teacher(school_BJ,'wusir')
taibai = Teacher(school_SH,'TaiBai')

#创建学员

jesse = Student('jesse',25,'male')

#注册一个学校,选择一个班级,缴纳学费
jesse.Enroll(school_BJ)
jesse.Choose_Class(class_201904)
jesse.Pay_tuition(16000)

#讲师视图.....

# 选择一个班级
alex.Choose_class(class_201904)
#查看这个班级的所有学生
alex.Get_class_student(class_201904)
#给这个班级的jesse学生评成绩
alex.Change_score(jesse)














