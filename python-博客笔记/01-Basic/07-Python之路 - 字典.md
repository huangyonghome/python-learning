# Python之路 - 字典

## 介绍  🍀

字典是一种key - value 的数据类型 , 用 冒号 (" : ") 来分割 , 每个对象之间用逗号(" , ")分割 , 整个字典包括在花括号("{ }")中

字典中的键(key)是唯一的 , 但值(value)则不必

**字典是可变的数据类型 , 并且是无序的**

> 从python3.6版本开始.字典是有序的

基本操作如下 : **创建、增加、修改、删除、查找、遍历、多级嵌套**等

注意 : 字典中key是唯一的 , 如果出现多个相同的key被赋值 , 那么值为最后一个赋的值 ; key是不可变的 , 所以可变的数据类型是不能用的 , 如 : list , 对于不可变的数据类型则可以 , 如 : str、int、tuple

2）key是不可变的 , 所以可变的数据类型是不能用的 , 如 : list , 对于不可变的数据类型则可以 , 如 : str、int、tuple

## 创建  🍀

```python
# 创建一个空字典
empty_info = {}
# 创建一个字典
info = {"name":"Lyon","age":21}
# 也可调用dict()方法
info = dict()
```

## 增加  🍀

```python
#创建字典
dic = {"name":"jesse","age":33,"job":"it","sex":"male"}

# 增加键值对
#给字典增加一个新的键值对.如果键不存在,则添加
dic['company'] = 'dwd'
print(dic)

>>> {'name': 'jesse', 'age': 33, 'job': 'it', 'sex': 'male', 'company': 'dwd'}

#如果字典已经存在了这个键.则用新的值替代
dic['company'] = 'hsq'
print(dic)

>>> {'name': 'jesse', 'age': 33, 'job': 'it', 'sex': 'male', 'company': 'hsq'}

#通过setdefault方法也可以增加一个值
dic.setdefault('school',"college")
print(dic)

>>>{'name': 'jesse', 'age': 33, 'job': 'it', 'sex': 'male', 'company': 'hsq', 'school': 'college'}

#和刚才相反.如果键已经存在,则新值不会生效.
dic.setdefault('school','primary')
print(dic)

>>>{'name': 'jesse', 'age': 33, 'job': 'it', 'sex': 'male', 'company': 'hsq', 'school': 'college'}

#update方法也可以修改字典键值对.如果键已经存在,则修改值,如果不存在,则添加
dic.update({"name":"Lyon","company":"internet"})
```

## 修改  🍀

```python
# 创建一个字典
info = {"name":"Lyon","age":21,"school":"university"}
# 修改age
info["age"] = 18
# 打印info
print(info)     
'''
执行结果:
{'age': 18, 'school': 'university', 'name': 'Lyon'}
'''
```

## 删除  🍀

```python
# 创建一个字典
dic = {"name":"jesse","age":33,"job":"it","sex":"male"}

# 1.pop()删除法
dic.pop('name')
print(dic)
# 注意pop方法有返回值
print(dic.pop('name'))
>>> jesse

2.del删除方法
del dic['name']
print(dic)
>>> {'age': 33, 'job': 'it', 'sex': 'male'}

# popitem删除法.(默认只删除最后一个)
dic.popitem()
print(dic)

>>> {'name': 'jesse', 'age': 33, 'job': 'it'}
```

## 查找  🍀

```python
# 创建一个字典
info = {"name":"Lyon","age":21,"school":"university"}

#1.查找键是否存在于字典中
print('name' in dic)
print('jesse' in dic)

>>> True
False

#2.获取键的值
print(dic['name'])
>>> jesse
#注意.如果字典中没有这个键,程序会报错
print(dic['jesse'])
>>> KeyError: 'jesse'

# get方法优雅的获取字典中某个键的值
print(dic.get('name'))
>>> jesse

#如果没有这个键,则返回none.但是程序不会报错
print(dic.get('jesse'))
>>> None
```

## 遍历  🍀

```python
# 创建一个字典
info = {"name":"Lyon","age":21,"school":"university"}
# 方法1,推荐
for key in info:
  print(key,info[key])
  
# 方法2
for k,v in info.items():
  print(k,v)
'''
执行结果:
school university
name Lyon
age 21
school university
name Lyon
age 21
'''
```

## 嵌套  🍀

```python
# 创建一个多级嵌套字典
dics = {
    'name':{
        'jesse':{
            'age':22,
            'job':'it',
            'sex':'male'
        },
        'jerry':{
            'age':23,
            'job':'it',
            'sex':'female'
        },

    },
    'home': {
        'jesse':{
            'live':'shanghai',
            'hometown':'jiangxi'
        },
        'jerry':{
            'live':'beijing',
            'hometown':'wuhan'
        }
    },
    'company':{
        'jesse':{
            'name':'dwd',
            'industry': 'internet'
        },
        'jerry':{
            'name': 'bat',
            'industry': 'internet'
        }
    }
}
# 修改最里层的value
dics['name']['jesse']['age'] = 33
print(dics['name']['jesse'])

>>>{'age': 33, 'job': 'it', 'sex': 'male'}
```

## 更多  🍀

```python
len(dict)        # 计算字典元素个数
dict.clear()     # 清空词典所有条目
dict.fromkeys(seq, val))  # 创建一个新字典,以列表 seq 中元素做字典的键,val 为字典所有键对应的初始值
dict.has_key(key)  # 如果键在字典dict里返回true,否则返回false
dict.items()       # 以列表返回可遍历的(键, 值) 元组数组
dict.keys()        # 以列表返回一个字典所有的键
dict.values()      # 以列表返回字典中的所有值
dict.setdefault(key, default=None) # 和get()类似, 但如果键不存在于字典中,将会添加键并将值设为default
dict.update(dict2)                 # 把字典dict2的键/值对更新到dict里
```
方法合集

```python
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
```
---

### 作业

##### 1.将下列字典中的key键含有'k'元素的所有键值对删除

```
#下面的方法报错..."RuntimeError: dictionary changed size during iteration"
#注意,字典在循环或者迭代的时候,不能修改该字典的内容.

dic = {'k1':'v1',"k2":'v2',"k3":'v3','name':'jesse'}

for k in dic:
    if 'k' in k:
        del dic[k]

print(dic)

#但是可以在循环一个列表的时候修改该字典

#新建一个空列表
l1 = []

#循环列表,将满足要求的key键添加进一个列表
for k in dic:
    if 'k' in k:
        l1.append(k)

#循环列表,这里就是循环字典的KEY..然后删除dic的键
for keys in l1:
    del dic[keys]

print(dic)
```