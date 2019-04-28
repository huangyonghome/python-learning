# Python之路 - 列表

## 介绍  🍀

列表是我们以后最常用的数据类型之一 , 通过列表可以对数据实现最方便的存储、修改等操作

**列表是可变的、有序的 ** , 基本操作有 : 创建、访问、切片、追加、插入、修改、删除、扩展、拷贝、排序、翻转、等

列表相当于其他语言中的数组

## 创建  🍀

```python
# 创建一个列表
names = ["Alex","Lyon","Leon"]
# 创建一个空列表
names = []
# 也可通过list方法
names = list()
```

## 访问  🍀

```python
#1.通过索引查找元素

# 创建一个列表
names = ["Alex","Lyon","Leon"]
# 与字符串的索引一样,列表索引从0开始,访问列表中的第一个元素
fristname = names[0]
# 打印结果
print(fristname)
# 访问列表中第三个元素
threename = names[2]
# 打印结果
print(threename)
# 访问列表中最后一个元素
endname = names[-1]
# 打印结果
print(endname)
# 访问倒数第二个元素
penultimate = names[-2]
# 打印结果
print(penultimate)
'''
执行结果:
Alex
Leon
Leon
Lyon
'''

#2.通过元素查找索引.index()方法
print(name.index('jesse'))
>>> 0

#3.#len函数查找列表的长度
print(len(name))
>>> 4

#4.count函数,查找某个元素在列表里出现的次数
print(name.count('jesse'))
>>> 1

```

**获取下标**

```python
# 创建一个列表
names = ['Alex', 'Lyon', 'Leon', 'CTO','Lyon']
# 获取下标并打印
print(names.index('Lyon')) 
# 注:只返回找到的第一个下标
'''
执行结果:
1
'''
```

**统计**

```python
# 创建一个列表
names = ['Alex', 'Lyon', 'Leon', 'CTO', 'BeiJing',"IT",21,"man"]
# 统计 "Lyon" 的个数,并打印
print(names.count("Lyon"))   
'''
执行结果:
1
'''
```

## 切片  🍀

```python
# 创建一个列表
names = ["Alex","Lyon","Leon","CTO","WuHan"]
# 取下标为1至下标3之间的值,包括1,不包括4
cutnames1 = names[1:3]
# 打印cutnames1
print(cutnames1) 
# 取下标为1至-1的值,不包括-1（-1就是最后一个）
cutnames2 = names[1:-1]
# 打印cutnames2
print(cutnames2)  
# 从第一个到第三个
cutnames3 = names[0:3]
# 从头开始取,0可以省略,跟上面的效果一样
cutnames4 = names[:3]
# 打印cutnames3,cutnames4
print(cutnames3,cutnames4) 
# 想取最后一个,只能这样写,切片是不包含后一个参数的
cutnames5 = names[3:]
# 后面的2是代表,每隔一个元素,就取一个
cutnames6 = names[0::2]
# 或者这样
cutnames7 = names[::2]
# 打印cutnames6,cutnames7
print(cutnames6,cutnames7) 
'''
执行结果:
['Lyon', 'Leon']
['Lyon', 'Leon', 'CTO']
['Alex', 'Lyon', 'Leon'] ['Alex', 'Lyon', 'Leon']
['Alex', 'Leon', 'WuHan'] ['Alex', 'Leon', 'WuHan']
'''
```

## 追加  🍀

```python
# 创建一个列表
names = ["Alex","Lyon","Leon","CTO","WuHan"]
# 追加一个元素
names.append("New")
# 打印names
print(names)
# 注：append 方法只能追加到列表的最后一位
'''
执行结果:
['Alex', 'Lyon', 'Leon', 'CTO', 'WuHan', 'New']
'''
```

> 注意,对列表的任何修改都是在原列表上进行的.而且所有方法都不会返回任何值.所以下面的例子返回None:

```
>>> name = ['jesse','Lyon','alex','jerry']
>>> name1=name.append('new')
>>> print(name1)
None
```



## 插入  🍀

```python
name = ['jesse','Lyon','alex','jerry']
#insert需要指定下标.
name.insert(1,'insert')
print(name)

#如果下标不存在就插入到最后一个
name.insert(111,'no one')
print(name)
```



## 修改  🍀

```python
# 创建一个列表
names = ['Alex', 'Insert', 'Lyon', 'Leon', 'CTO', 'WuHan', 'New', 'NoIndex']
# 把 'WuHan' 改成 'BeiJing'
names[5] = 'BeiJing'
# 打印names
print(names)
# 注：就是通过下标直接改变list本身
'''
执行结果:
['Alex', 'Insert', 'Lyon', 'Leon', 'CTO', 'BeiJing', 'New', 'NoIndex']
'''
#切片修改
name[:2] = "huang"
print(name)
>>> ['h', 'u', 'a', 'n', 'g', 'alex', 'jerry']

#分别赋值,将3个元素分别赋值.
name[:3] = "a","b","c"
print(name)
>>> ['a', 'b', 'c', 'Lyon', 'alex', 'jerry']

#也可以用元祖的3个元素分别赋值
name[:3] = ("x","y","z")
print(name)
>>> ['x', 'y', 'z', 'Lyon', 'alex', 'jerry
```


## 删除  🍀

```python
name = ['jesse','Lyon','alex','jerry']
#1.按照索引删除.pop()方法
name.pop(1)
print(name)
>>> ['jesse', 'alex', 'jerry']

#注意pop方法有返回值,返回的是删除的那个元素.例如
print(name.pop(1))
>>> Lyon

#如果不指定索引,则删除最后一个
name.pop()
print(name)
>>> ['jesse', 'Lyon', 'alex']

#2.删除一个指定的真实元素.remove()方法
name.remove('jesse')
print(name)
>>> ['Lyon', 'alex', 'jerry']

##3.支持切片删除方法
#删除单个索引
del name[1]
print(name)
>>> ['jesse', 'alex', 'jerry']

#删除切片
del name[1:]
print(name)
>>> ['jesse']

#4.清空列表.clear()方法
name.clear()
print(name)
>>>[]
```

## 扩展  🍀

```python
# 创建一个列表
names = ['Alex', 'Lyon', 'Leon', 'CTO', 'BeiJing']
# 创建另一个列表
name = ["IT",21,"man"]
# 将name扩展到names
names.extend(name)
# 打印names
print(names)  
# 这里还有一个"万恶的'+' "也是可以的
print(names + name) 
'''
执行结果:
['Alex', 'Lyon', 'Leon', 'CTO', 'BeiJing', 'IT', 21, 'man']
['Alex', 'Lyon', 'Leon', 'CTO', 'BeiJing', 'IT', 21, 'man']
'''
```

## 拷贝  🍀

```python
# 创建一个列表
names = ['Alex', 'Lyon', 'Leon', 'CTO', 'BeiJing',"IT",21,"man"]
# 拷贝names,这只是浅copy
names_copy = names.copy()  
# 打印names_copy
print(names_copy)   
'''
执行结果:
['Alex', 'Lyon', 'Leon', 'CTO', 'BeiJing', 'IT', 21, 'man']
'''
```

注意 : 在python2.7中列表的内置方法是没有copy这个方法的 , 这是在python3后加的 , 并且python3也只有有copy (浅copy) 这一个方法 , 用深copy需要我们导入copy模块 , 即 import copy 

深浅copy会在后续文章中整理　

## 排序&翻转  🍀

```python
# 创建一个列表
names = ['Alex', 'Lyon', 'Leon', 'CTO', 'BeiJing',"IT",21,"man"]
# 在python3中不同的数据类型不能一起排序,换成str
names[-2] = "21"
# 排序,顺序为数字>大写>小写
names.sort()
# 打印names
print(names)    
# 翻转
names.reverse()
# 打印names
print(names)      
'''
执行结果:
['21', 'Alex', 'BeiJing', 'CTO', 'IT', 'Leon', 'Lyon', 'man']
['man', 'Lyon', 'Leon', 'IT', 'CTO', 'BeiJing', 'Alex', '21']
'''
```

所有方法如下 : 

```python
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
```

---

## 练习题  🍀

```

name = ['jesse','Lyon','alex','jerry',[1,'tony']]


#1.将jesse变成大写
name[0] = name[0].upper()
print(name)

#2.将tony变成首字母大写
str = name[-1][-1].capitalize()
name[-1][-1] = str
print(name)
```

* 3.将下列列表中奇数索引的元素删除

```
l1 = [00,11,22,33,44,55,66]

#方法一.采取步长方式.这也是最简单有效的方式

print(l1[::2])
>>> [0, 22, 44, 66]

#方法二.判断是否能被2整除..因为列表是可变的,对列表的任何修改都会得到预期之外的结果.所以不能对列表进行直接操作

#新建一个空列表

l2 = []

#循环l1的索引,偶数元素加入到l2.

for num in range(len(l1)):
     if num % 2 == 0:
         l2.append(l1[num])

#打印l2
print(l2)
>>> [0, 22, 44, 66]

#方法三..倒序循环列表,可以直接修改.因为修改列表(删除列表元素)对循环的索引没有影响.

#注意,起始索引是列表长度-1,然后截止索引是-1,而不是0,步长是-1
for num in range(len(l1)-1,-1,-1):
    if num % 2 == 1:
        del l1[num]

print(l1)
>>> [0, 22, 44, 66]
```