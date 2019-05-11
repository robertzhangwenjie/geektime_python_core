#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/11 9:06
# @Author   :   robert
# @FileName :   calculator.py
# @Software :   PyCharm
import re


class Calculator(object):

    def add(self,arg_a,arg_b):
        return arg_a + arg_b

    def sub(self,arg_a,arg_b):
        return arg_a - arg_b

    def division(self,arg_a,arg_b):
        return arg_a/arg_b

    def multi(self,arg_a,arg_b):
        return arg_a * arg_b


    def run(self):
        while True:
            args = input('请输入运算公式:')
            ret = re.search(r'[^0-9+-/*]',args)
            if ret:
                print('只支持数字运算')
                continue
            if '+' in args:
                arg_list = args.split('+')
                arg_a = arg_list[0].strip()
                arg_b = arg_list[1].strip()
                if arg_a and arg_b:
                    print(self.add(int(arg_a), int(arg_b)))
                else:
                    print('输入不合法！useage: a +/*- b')
                    continue
            elif '-' in args:
                arg_list = args.split('-')
                arg_a = arg_list[0].strip()
                arg_b = arg_list[1].strip()
                if arg_a and arg_b:
                        print(self.sub(int(arg_a),int(arg_b)))
                else:
                    print('输入不合法！useage: a +/*- b')
                    continue
            elif '*' in args:
                arg_list = args.split('*')
                arg_a = arg_list[0].strip()
                arg_b = arg_list[1].strip()
                if arg_a and arg_b:
                    print(self.multi(int(arg_a), int(arg_b)))
                else:
                    print('输入不合法！useage: a +/*- b')
                    continue
            elif '/' in args:
                arg_list = args.split('/')
                arg_a = arg_list[0].strip()
                arg_b = arg_list[1].strip()
                if arg_a and arg_b:
                    print(self.division(int(arg_a), int(arg_b)))
                else:
                    print('输入不合法！useage: a +/*- b')
                    continue

            else:
                print('useage: a +/*- b')
                

if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()