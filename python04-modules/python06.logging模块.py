# -*- coding: utf-8 -*-
# @Time    : 2019-06-15 11:46
# @Author  : jesse
# @File    : python06.logging模块.py

import logging
'''
logging模块简单用法
'''

# #自定义日志输出格式
#
# #level:输出日志级别
# #format:日志输出格式串
# #datefmt:时间日期格式
# #filename.保存文件路径.日志打开模式默认为a
# logging.basicConfig(level=logging.WARNING,
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s",
#                     datefmt = '%Y-%m-%d  %H:%M:%S',
#                     filename='sys.log'
#                     )
#
# #下面定义了5个logging级别的日志.默认只输出warrning级别以上的日志
# logging.debug("debug调试")
# logging.info("正常日志信息")
# logging.warning("警告信息")
# logging.error("错误信息")
# logging.critical("严重错误")


'''
logging模块进阶日志流处理
'''

# import logging
#
# #step1: 创建logger对象.如果参数为空,则返回root logger
# logger = logging.getLogger()
#
# #step2: 设置logger日志等级.可以是级别名,还可以是数字
#
# logger.setLevel(logging.DEBUG)
#
# #step3: 创建输出流对象
#
# #创建handler文件句柄对象
# fh = logging.FileHandler('test.log',encoding='utf-8')
# #创建控制台输出对象
# sh = logging.StreamHandler()
#
# #step4.定义日志格式
#
# formatter = logging.Formatter(
#     fmt="%(asctime)s %(name)s %(filename)s %(message)s",
#     datefmt="%Y/%m/%d %X"
#     )
#
#
# #step5.输出流对象和日志格式进行关联.格式化日志输出
#
# fh.setFormatter(formatter)
# sh.setFormatter(formatter)
#
# #step6. 添加输出流对象和logger对象
#
# logger.addHandler(fh)
# logger.addHandler(sh)
#
# #step7: 输出日志
#
# logger.debug("debug调试")
# logger.info("正常日志信息")
# logger.warning("警告信息")
# logger.error("错误信息")
# logger.critical("严重错误")


'''logging模块重复打印日志'''

# import logging
#
# def log(msg):
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#
#     fh = logging.FileHandler('test.log',encoding='utf-8')
#     sh = logging.StreamHandler()
#
#     formatter = logging.Formatter(
#         fmt="%(asctime)s %(name)s %(filename)s %(message)s",
#         datefmt="%Y/%m/%d %X"
#         )
#
#
#     fh.setFormatter(formatter)
#     sh.setFormatter(formatter)
#
#     logger.addHandler(fh)
#     logger.addHandler(sh)
#
#     logger.info(msg)
#
# #解决重复打印日志方法:每次调用完就关闭文件句柄
#     # logger.removeHandler(fh)
#     # logger.removeHandler(sh)
#
#
#
# log("前方注意")
# log("提示")
# log("错误")

# '''
# 原因：第二次调用log的时候，根据getLogger(name)里的name获取同一个logger，
# 而这个logger里已经有了第一次你添加的handler，第二次调用又添加了一个handler，
# 所以，这个logger里有了两个同样的handler，以此类推，调用几次就会有几个handler。
# '''
#
# #第二种解决方法.每次创建文件句柄对象时,先判断是否已经存在一个对象
#
# import logging
#
# def log(msg):
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#
#     #解决方案2.handlers对象,如果没有就创建.否则直接记录日志
#     if not logger.handlers:
#         fh = logging.FileHandler('test.log',encoding='utf-8')
#         sh = logging.StreamHandler()
#
#         formatter = logging.Formatter(
#             fmt="%(asctime)s %(name)s %(filename)s %(message)s",
#             datefmt="%Y/%m/%d %X"
#             )
#
#
#         fh.setFormatter(formatter)
#         sh.setFormatter(formatter)
#
#         logger.addHandler(fh)
#         logger.addHandler(sh)
#
#     logger.info(msg)
#
#
#
#
# log("前方注意")
# log("提示")
# log("错误")
#
#
# '''
# 完整调用方式:
# '''
#

# import logging
#
# def log():
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#
#     #解决方案2.handlers对象,如果没有就创建.否则直接记录日志
#     if not logger.handlers:
#         fh = logging.FileHandler('test.log',encoding='utf-8')
#         sh = logging.StreamHandler()
#
#         formatter = logging.Formatter(
#             fmt="%(asctime)s %(name)s %(filename)s %(message)s",
#             datefmt="%Y/%m/%d %X"
#             )
#
#
#         fh.setFormatter(formatter)
#         sh.setFormatter(formatter)
#
#         logger.addHandler(fh)
#         logger.addHandler(sh)
#
#     return logger
#
#
#
#
# log_record = log()
# log_record.info('前方注意')
# log_record.error('前方报错')
# log_record.debug('前方正常')



'''
logging模块高级进阶

将上述配置定义在一个logging字典中.然后用该字典实例化一个logger对象.
'''

import os
import logging.config

# 定义三种日志输出格式 开始

standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'advance.log'  # log文件名

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    #定义2个日志格式
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(__name__)  # 生成一个log实例
    return logger
    # logger.info('It works!')  # 记录该文件的运行状态

log = load_my_logging_cfg()
log.info("程序正常")