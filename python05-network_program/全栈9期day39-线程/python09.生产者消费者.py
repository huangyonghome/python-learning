# -*- coding: utf-8 -*-
# @Time    : 2020-06-21 11:21
# @Author  : jesse
# @File    : python09.生产者消费者.py


#基础版

# import threading
# import queue
# def producer():
#     for i in range(10):
#         # 进行生产,放入队列
#         q.put("%d bottle of milk" % i)
#     print("Start waiting for all the milk to be taken...")
#     q.join()
#     print("All the milk was taken out...")
#
# def consumer(name):
#     # 队列中有就取
#     while q.qsize() > 0:
#         print("%s got %s" % (name, q.get()))
#         q.task_done()
# # 创建一个队列对象
# q = queue.Queue()
# p = threading.Thread(target=producer,)
# p.start()
# c1 = consumer("Lyon")





#高级版

import time
import random
import queue
import threading
q = queue.Queue()
def Producer(name):
  count = 1
  while count < 20:
    time.sleep(random.randrange(3))
    # 将数据放入队列
    q.put(count)
    print('Producer %s has produced %s bun...' % (name, count))
    count += 1
def Consumer(name):
  count = 1
  while count < 20:
    time.sleep(random.randrange(4))
    # 不为空就取,为空就提示
    if not q.empty():
        # 从队列中取出信息
        data = q.get()
        print(data)
        print('\033[32;1mConsumer %s has eat %s bun...\033[0m' % (name, data))
    else:
        print("No bun anymore...")
    count += 1
p1 = threading.Thread(target=Producer, args=('Lyon',))
c1 = threading.Thread(target=Consumer, args=('Kenneth',))
p1.start()
c1.start()