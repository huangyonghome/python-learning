#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/4 下午8:23
# @Author  : jesse
# @File    : yield.py

# yield生成器讲解博客
# https://blog.csdn.net/mieleizhi0522/article/details/82142856


# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))
# print("*"*20)
# print(next(g))

# def bar():
#     print('test')
#     while True:
#         res = yield 4
#         print(res)
#
#
# b = bar()
#
# print(b)
# print(next(b))
# print(b.send(7))


# 生成器本身也遵循迭代协议,也就意味着可以使用python内置的sum,for等循环.

# Python有两种方式提供生成器:
# 1.生成器函数:
#   使用yield返回结果,而不是return.yield的函数并不会调用的时候立即执行,而是返回一个yield生成器对象.
#   只有当调用next方法时,才会真正执行函数.
#   (1).延迟操作.只有需要的时候(next)才产生结果,而不是立即产生结果.
#   (2).yield一次返回一个结果,返回结果后挂起函数状态.下次执行(next方法)的时候,又从函数上一次执行的原处开始执行

# 2.生成器表达式:
#   类似于列表推导,但是,生成器返回按需产生结果的一个对象,而不是一次构建一个结果列表



# 1. 下面的例子中演示了普通函数和yield生成器函数的区别

# 计算下面text字符串中的空格的索引位置,如果使用普通函数,需要将索引(index)添加到一个列表中.然后返回列表
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index,letter in enumerate(text,1):
        if letter == ' ':
            result.append(index)

    return result


text = """The Zen of Python, by Tim Peters"""
print(index_words(text))


#下面是使用yield生成器函数实现上面的需求.yield每次返回一个索引(index).而不需要事先将所有索引找到.
def generator_words(text):
    if text:
        yield  0

    for index,letter in enumerate(text,1):
        if letter == ' ':
            yield index

print([x for x in generator_words(text)])
print(list(generator_words(text)))


# 2.生成器表达式

# 下面是一个列表推导式

squares = [x**2 for x in range(5)]

print(squares)

# 将列表推导式的中括号替换成圆括号,就是一个生成器表达式

squares = (x**2 for x in range(5))

print(squares)

# 调用next方法获取生成器中的值
print(next(squares))
print(next(squares))

# 由于执行了2次next方法,所以下面将生成器值转换成列表时,从第三个值开始
print(list(squares))



### sum函数也可以使用生成器

print(sum((x**2 for x in range(4))))

### 为了简单起见,也可以省略生成器的圆括号
print(sum(x**2 for x in range(4)))

## 当然使用列表推导式也可以

print(sum([x**2 for x in range(4)]))

### 使用生成器的主要原因是,生成器支持延时计算.所谓延时计算就是一次返回一个结果,而不是一次返回所有结果
### 比如下面2个表达式,列表推导式一次生成所有结果,计算机内存很快就会耗光..
## 而生成器由于一次返回一个值,所以执行速度非常快,几乎没有内存占用

sum([i for i in range(100000000000000000000)])
sum(i for i in range(10000000000000000000000))