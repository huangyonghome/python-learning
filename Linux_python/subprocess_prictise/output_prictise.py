#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 下午5:33
# @Author  : jesse
# @File    : output_prictise.py

import subprocess

# check_output函数和call一样,但是不直接将命令结果输出到终端
output = subprocess.check_output("df -h", shell=True)

output1 = subprocess.check_output(['df','-h'])

#输出结果需要decode
result = output.decode('utf-8')

lines = result.split('\n')

line_dict={}


#筛选出挂载点和磁盘使用率
for line in lines[1:-1]:
    if line:
        # print(line)
        # print(line.split()[:-3:-1])
        line_dict[line.split()[-1]] = line.split()[-2].split('%')[0]


print(line_dict)

#找出磁盘使用率低于50的分区
for k,v in line_dict.items():
    if int(v) <= 50:
        print(k,v)



# 如果命令直接结果不为1.则直接抛出异常

# output = subprocess.check_output('ps uax | grep php-fpm | grep -v grep',shell=True)
# print(output)


#异常情况处理

try:
    output = subprocess.check_output('ps uax | grep php-fpm | grep -v grep',shell=True,stderr = subprocess.STDOUT)

except subprocess.CalledProcessError as e:
    output = e.output
    code = e.returncode

    print(output,code)