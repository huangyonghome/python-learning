 # -*- coding: utf-8 -*-
# @Time    : 2019-06-08 12:25
# @Author  : jesse
# @File    : education.py

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

import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

class Education():
    def __init__(self, name):
        #继承通用name属性
        self.name = name

    def show_info(self):
        pass

    def __str__(self):
        #打印任何类的实例对象的时候返回该类的name值
        return self.name


class School(Education):

    def __init__(self,name,city):
        #初始化school.包含2个信息:学校名和学校地址
        super().__init__(name)
        self.city = city
        self.classes = []
        self.course = []
        self.students = []
        self.teachers = []

    def show_info(self):
        #打印学校信息,包括学校名,课程,老师
        print("school:name: %s" %self.name)
        if self.course:
            for k in self.course:
                print("course:%s" %k.name)
        else:
            print("course:%s" %self.course)

        if self.teachers:
            for k in self.teachers:
                print("teachers:%s" % k.name)
        else:
            print("teachers:%s" % self.teachers)

        if self.students:
            for k in self.students:
                print("students:%s" % k.name)
        else:
            print("students:%s" % self.students)

    def enroll(self,student):
        # 学员注册
        self.students.append(student)
        print("%s enroll in %s "% (student.name, self.name))

    def leave_school(self, student):  # 退学
        self.students.remove(student)
        print("%s leave school from %s " % (student.name, self.name))

    def hire_teacher(self, teacher):
        #学校实例增加老师,这里是teacher对象,不是老师名
        self.teachers.append(teacher)
        print("teacher: %s hire successful" % teacher.name)

    def fire_teacher(self, teacher):
        self.teachers.remove(teacher)
        print("teacher: %s fired from %s" % (teacher.name, self.name))

    def create_class(self,name,teacher,course):
        # 创建班级.班级关联课程,老师,学校
        #通过学校创建班级.将班级实例化对象添加进self.classes
        classes = Classes(name, teacher, course)
        self.classes.append(classes)
        print("classes %s create successful" % name)
        return classes #返回创建的实例化对象

    def create_course(self, name, cycle, price):
        """ 课程包含，周期，价格，通过学校创建课程"""
        # 通过学校创建课程.将课程实例化对象添加进self.course
        course = Course(name, cycle, price)
        self.course.append(course)
        print("course: %s create successful" % name)
        return course #返回创建的实例化对象

    def create_teacher(self, name):
        # 通过学校创建老师.将老师实例化对象添加进self.teachers
        teacher = Teacher(name, self)
        self.teachers.append(teacher)
        print("teacher: %s create successful" % name)
        return teacher #返回创建的实例化对象


class Classes(Education):
    def __init__(self,name,teacher,course):
        #班级包含班级名,老师,课程,以及学生
        super().__init__(name)
        self.teacher = teacher
        self.course = course
        self.students = []

    def enroll(self, student):  # 学员注册
        self.students.append(student)
        print("%s enroll in %s " % (student.name, self.name))

    def leave_grade(self, student): # 学员离开
        self.students.remove(student)
        print("%s leave grade from %s " % (student.name, self.name))

    def show_info(self):
        #打印班级信息
        print("grade:name: %s\t teacher:%s\t course:%s\t students:%s"%
              (self.name, self.teacher, self.course, self.students))

class Course(Education):
    #课程类包含课程名,周期,价格
    def __init__(self,name,cycle,price):
        super().__init__(name)
        self.cycle = cycle
        self.price = price


class Student(Education):
    """学生
    5. 创建学员时，选择学校，关联班级
    """
    def __init__(self, name, school, classes, score=0):
        super().__init__(name)
        self.score = score
        self.tuition = 0
        self.school = None
        self.classes = None
        self.choose_school(school)
        self.choose_classes(classes)

    # 6.1 学员视图， 可以注册， 交学费， 选择班级，
    def choose_school(self, school):
        school.enroll(self)
        self.school = school

    def choose_classes(self,classes):
        #通过班级类修改学生信息
        if self.classes !=None:
            self.classes.leave_grade(self)
        classes.enroll(self)
        self.classes = classes

    def pay_tuition(self, money):
        self.tuition += money

    def show_info(self):
        print("student:name: %s\t school:%s\t grade:%s\t score:%s\t tuition:%s"%
              (self.name, self.school, self.classes, self.score, self.tuition))



class Teacher(Education):
    """老师
     创建讲师角色时要关联学校，
    """
    def __init__(self, name, school):
        super().__init__(name)
        self.school = None
        self.classes = None
        self.name = name
        self.choose_school(school)

    # 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级，
    # 查看班级学员列表 ， 修改所管理的学员的成绩
    def choose_school(self, school):
        if self.school != None:
            self.school.fire_teacher(self)
        school.hire_teacher(self)
        self.school = school

    def choose_classes(self, classes):
        self.classes = classes

    def show_students(self):
        if self.classes != None:
            for student in self.classes.students:
                student.show_info()
        else:
            print("当前班:%s,没有任何学生" %self.classes)

    def modify_score(self, student, score):
        student.score = score

    def show_info(self):
        print("teacher:name: %s\t school:%s\t classes:%s"%
              (self.name, self.school, self.classes))


if __name__ == "__main__":
    school = School('武汉大学','湖北')
    teacher = school.create_teacher('王老师')
    course = school.create_course('数学','1年','2222')
    classes = school.create_class("高三",teacher,course)
    student = Student("Tom", school, classes)
    student.show_info()
    teacher.show_info()
    print("school:",school.students)