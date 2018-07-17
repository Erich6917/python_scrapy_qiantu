# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 
# @Author  : ErichLee ErichLee@qq.com
# @File    : logger_util.py
# @Comment : 打印工具
#


def infos(*args):
    if args:
        str_list = []
        for each in args:
            str_list.append(str(each))
        msg = ' '.join(str_list)
        print_new_line(msg)
        # logging.info(args)


def print_new_line(msg):
    print(msg)


def print_no_line(msg):
    print(msg, end='')


def ljinfos(lmgs, *args):
    """
    :param lmgs: 左对齐打印头 需要格式化长度
    :param args: 变量参数依次打印
    """
    if lmgs:
        print_no_line('[{}]:'.format(lmgs.ljust(30)))
    else:
        print_no_line('[{}]'.format("".ljust(30)))

    if any(args):
        for each in args:
            print_no_line(each)
    print_new_line()


def cinfos(lmgs, *args):
    """
    :param lmgs: 居中打印头 需要格式化长度
    :param args: 变量参数依次打印
    """
    if lmgs:
        print_no_line('[{}]:'.format(lmgs.center(30)))
    else:
        print_no_line('[{}]'.format("".center(30)))

    if any(args):
        for each in args:
            print_no_line(each)
    print_new_line()


def println():
    print_new_line('================================================================')


def errors(*args):
    if args:
        str_list = []
        for each in args:
            str_list.append(str(each))
        msg = ' '.join(str_list)
        print_no_line('[ERROR]: {}'.format(msg))
