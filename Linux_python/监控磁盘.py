#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 上午9:41
# @Author  : jesse
# @File    : 监控磁盘.py

from collections import namedtuple

Disk = namedtuple('Disk', 'major_number minor_number device_name'
                   'read_count read_merged_count read_sections'
                   'time_spent_reading write_count write_merged_count'
                  'write_sections time_spent_write io_requests'
                  'time_spent_doing_io weighted_time_spent_doing_io')
#
# Disk = namedtuple('Disk', 'major_number minor_number device_name'
#                           ' read_count read_merged_count read_sections'
#                           ' time_spent_reading write_count write_merged_count'
#                           ' write_sections time_spent_write io_requests'
#                           ' time_spent_doing_io weighted_time_spent_doing_io')

def get_disk_info(device):
    '''
    从/proc/diskstats文件中读取磁盘信息
    [work@idc-beta-docker ~]$ cat /proc/diskstats
8 3 sda3 40030528 477185 6875171252 399533243 140845213 10515741 22819797720 370773022 0 121871093 768647600
    '''
    with open('diskstats') as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split()))
        raise RuntimeError("device ({0}) not found!".format(device))


def main():
    disk_info = get_disk_info('sda3')
    print(disk_info)
    print("磁盘写次数:{}".format(disk_info.write_count))


if __name__ == '__main__':
    main()