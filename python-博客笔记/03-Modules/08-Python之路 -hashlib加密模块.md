# Python之路 - hashlib加密

##  介绍 🍀

此模块有人称为摘要算法，也叫做加密算法，或者是哈希算法，散列算法等等，这么多title不用大家记，那么有同学就问他到底是干啥的？ 简单来说就是做加密和校验使用，它的工作原理给大家简单描述一下：它通过一个函数，把任意长度的数据按照一定规则转换为一个固定长度的数据串（通常用16进制的字符串表示）。


#### hashlib的特征以及使用要点：

1.bytes类型数据 ---> 通过hashlib算法 ---> 固定长度的字符串

2.不同的bytes类型数据转化成的结果一定不同。

3.相同的bytes类型数据转化成的结果一定相同。

4.此转化过程不可逆。


#### hashlib的主要用途有两个：

1.密码的加密。

2.文件一致性校验。


##  普通密码加密 🍀

这里以md5加密方式为例.加密步骤非常简单.只需要3个步骤:

```
str1 = "jesse"

#1.实例化一个对象
md5 = hashlib.md5()

#2.调用update方法给字符串加密
md5.update(str1.encode('utf-8'))

#3.打印加密后的值. #a1361cb85be840d6a2d762c68e4910e2
print(md5.hexdigest())
```
上面就是普通的md5加密，非常简单，几行代码就可以了.将jesse字符串加密成MD5密文,用于存储密码信息.


#### 如果需要加密的数据量很大,可以多次update.然后最后得出加密字符串

```
res = hashlib.md5()
res.update("jesse".encode('utf-8'))
res.update("Lyon".encode("utf-8"))
print(res.hexdigest())  #f3e1e5c71241e50ff3e373e6243e125e
```
上面计算出来的MD5密文是jesseLyon这个字符串


## SHA加密算法 🍀

另一种常见的摘要算法是SHA，SHA有不同的加密复杂度计算,例如:sha1,sha224,sha512等等，数字越大，加密的方法越复杂，安全性越高，但是效率就会越慢。

调用SHA加密和调用MD5完全类似：

```
sha1 = hashlib.sha1()
sha1.update('jesse'.encode('utf-8'))
print(sha1.hexdigest())
```


## 加盐加密 🍀

但是简单的口令，可以非常容易的计算出这些常用口令的MD5值，得到一个反推表.这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。

对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

#### 固定加盐

```
salt = hashlib.md5("addtional_info".encode('utf-8'))
salt.update('jesse'.encode('utf-8')) #实际上是让jesse+addtional_info2个字符串一起加密.
print(salt.hexdigest())  #这样即使别人知道你密码,但是也无法知道MD5加密字符串
```

#### 动态的盐

但是如果黑客通过手段窃取到你这个固定的盐之后，也是可以破解出来的。所以，我们还可以动态的盐。

下面是用用户的username来为该用户的密码加盐:

```
username = input("请输入用户名:").strip()
password = input("请输入密码:").strip()

if username  and password:
    encrypt = hashlib.md5(username.encode("utf-8"))
    encrypt.update(password.encode("utf-8"))
    print(encrypt.hexdigest())
else:
    print("输入错误")

```
这样，安全性能就大大提高了。


### 利用hashlib给用户密码加密的一个例子

下面是加密算法在一个简单的用户登录程序中的使用

```
import hashlib,ast

def user_auth():
    ''' 计算用户密码的加密字符串'''

    username = input("请输入用户名:").strip()
    password = input("请输入密码:").strip()

    if username  and password:
        encrypt = hashlib.md5(username.encode("utf-8"))
        encrypt.update(password.encode("utf-8"))
        password = encrypt.hexdigest()
        return username,password
    else:
        print("输入错误")
        exit(1)


def register():
    '''注册用户'''

    username,password = user_auth()
    dic1 = {username:password}
    with open("user.db", 'w') as f:
        f.write(str(dic1))

def login():
    '''用户登录'''

    with open("user.db", 'r') as f:
        dic1 = f.read()
    # 将f.read()读取出来的字符串转换成字典.json.loads方法也可以实现,
    # 但是json模块要求是双引号的字符串.这里是一个单引号的字符串,所以需要ast模块
    dic1 = ast.literal_eval(dic1)
    username,password = user_auth()
    if username in dic1 and password == dic1[username]:
        print("恭喜登录成功")
    else:
        print("用户密码输入不正确")


dict2 = {"1":register,"2":login}

print('''
1:register,2:login
''')

choise = input("请输入序号:")

if choise in dict2:
    dict2[choise]()
else:
    print("输入错误")

```

## 文件校验 🍀

hashlib模块除了可以用于密码加密之外，还有一个常用的功能，那就是文件的一致性校验。文件校验通常用来比较2个文件是否是同一份文件

```
import os,hashlib

def file_check(file_path):
    file_md5 = hashlib.md5()

    if os.path.isfile(file_path):
        with open(file_path,'r') as f:

        #下面循环可以替换成:for line in f:
            for line in f.readlines():
                #循环文件,每次只update一行数据.避免一次加密整个文件造成系统崩溃
                file_md5.update(line.encode('utf-8'))
        return file_md5.hexdigest()
    else:
        print("文件不存在")



#复制2个一模一样的文件,计算出来的MD5值完全相同

print(file_check('文件校验1.log')) #cae4133f1d66a901a90cdafaf6172c07
print(file_check('文件校验2.log')) #cae4133f1d66a901a90cdafaf6172c07

#将文件校验2.log文件最后一行删除一个空格,再次计算.发现MD5值已经不一样

print(file_check('文件校验1.log'))  #cae4133f1d66a901a90cdafaf6172c07
print(file_check('文件校验2.log'))  #c48313c88156e33b7fc7ba21661dad59
```

