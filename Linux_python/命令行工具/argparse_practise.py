#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 上午11:09
# @Author  : jesse
# @File    : argparse_practise.py

import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("e")
# args = parser.parse_args()
# print(args.e)



# parser = argparse.ArgumentParser()
# parser.add_argument("-v","--verbosity", help="添加输出", action="store_true")
# args = parser.parse_args()
# if args.verbosity:
#     print("打开verbosity")


def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('--host', '-h', action='store', dest='server',  help='connect to host',required=True)
    parser.add_argument('-t', action='store_true', dest='boolean_switch', help='Set a switch to true')
    return parser.parse_args()


def main():
    parser = _argparse()
    print(parser)
    print('host =', parser.server)
    print('boolean_switch=', parser.boolean_switch)


if __name__ == '__main__':
    main()