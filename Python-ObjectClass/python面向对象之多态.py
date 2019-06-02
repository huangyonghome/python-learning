# -*- coding: utf-8 -*-
# @Time    : 2019-06-02 16:01
# @Author  : jesse
# @File    : python面向对象之多态.py

class Animal():
    pass
    # def run(self):
    #     print("Animal is running")



class Dog(Animal):
    def run(self):
        print("dog is running")





class Cat(Animal):
    def run(self):
        print("cat is running")


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


class Timer():
    def run(self):
        print("start")

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
cat = Cat()

# dog.run()
# cat.run()

run_twice(Tortoise())
run_twice(Timer())