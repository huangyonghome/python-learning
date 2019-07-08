# -*- coding: utf-8 -*-
# @Time    : 2019-06-23 9:38
# @Author  : jesse
# @File    : python02.进程.py


#!/usr/bin/python
# 孤儿进程和僵尸进程

'''
孤儿进程和僵尸进程的代码演示,以下代码在Linux系统中演示
孤儿进程和僵尸进程介绍:
https://www.cnblogs.com/JohnABC/p/5734571.html
'''

# 演示孤儿进程:当主进程退出,子进程仍然存在,这个时候被Linux的init进程认领

import os,time,sys


pid = os.getpid()
ppid = os.getppid()
print("i am father process,my pid is %s my ppid is %s"  %(pid,ppid))

pid = os.fork()
'''
#执行pid=os.fork()则会生成一个子进程
#返回值pid有两种值：
#    如果返回的pid值为0，表示在子进程当中
#    如果返回的pid值>0，表示在父进程当中
'''

if pid > 0:
   print("father process is dead")
   sys.exit(0)

#子进程仍然还存在
time.sleep(5)
print("I am child my pid %s my ppid is %s" %(os.getpid(),os.getppid()))


#执行结果:

'''

[root@localhost ~]$python3 test.py
i am father process,my pid is 16963 my ppid is 16230 
father process is dead
[root@localhost ~]$I am child my pid 16964 my ppid is 1  #父进程已经变成了int

'''

# 演示僵尸进程:当子进程退出,主进程没有调用wait()和waitpid()方法销毁子进程,这个时候子进程的部分信息仍然存在

import os,time,sys


pid = os.fork()
'''
#执行pid=os.fork()则会生成一个子进程
#返回值pid有两种值：
#    如果返回的pid值为0，表示在子进程当中
#    如果返回的pid值>0，表示在父进程当中
'''

#子进程已经执行结束了
if pid == 0:
    time.sleep(1)
    print("child process is done")
    sys.ext(0)

if pid > 0:
   print("father process is running ")
   time.sleep(10)  #但是主进程没有对子进程进行任何处理
   sys.exit(0)


'''
执行结果

root@localhost ~]$ps aux | grep Z
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root     17212  0.0  0.0      0     0 pts/0    Z+   13:06   0:00 [python3] <defunct>  #状态是Z,表示zombie进程
root     17214  0.0  0.1 112720  2252 pts/2    S+   13:06   0:00 grep --color=auto Z
[root@localhost ~]$top -b | head
top - 13:06:54 up 10 days,  3:48,  2 users,  load average: 0.00, 0.01, 0.00
Tasks: 164 total,   1 running,  64 sleeping,   4 stopped,   1 zombie                 #1个zombie状态


'''