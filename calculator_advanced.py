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
        '''
        思路进阶:1.使用正则表达式对args字符串进行匹配查看有哪些符号
        2.判断该符号是否只有一个
        3.如果符号只有一个，使用该符号进行切割
        :return:
        '''
        while True:
            args = input('请输入运算公式:')
            # 判断输入是否合法，注意减法'-'在[]中表示一个范围，如果要匹配到需要转义
            ret = re.search(r'[^0-9+\-/*]',args)
            # print(ret)
            if ret:
                print('只支持整数运算')
                continue
            # 正则匹配找出所有的符号个数
            op_str_num = re.findall(r'[+\-/*]', args)
            # print(op_str_num)
            # 判断是否只有一个运算符
            if not len(op_str_num) == 1:
                print('有多个运算符号或者没有运算符号')
                continue
            # 获取运算符
            op_str = op_str_num[0]
            print(f'正在进行"{op_str}"运算')
            # 以运算符进行分割,取出运算元素
            arg_list = args.split(op_str)
            arg_a = arg_list[0].strip()
            arg_b = arg_list[1].strip()

            # 判断运算符两边是否存在数据
            if arg_a and arg_b:
                if op_str == '+':
                    print(self.add(int(arg_a), int(arg_b)))
                elif op_str == '-':
                    print(self.sub(int(arg_a), int(arg_b)))
                elif op_str == '*':
                    print(self.multi(int(arg_a), int(arg_b)))
                elif op_str == '/':
                    print(self.division(int(arg_a), int(arg_b)))
            else:
                print('缺少运算对象')
                continue

if __name__ == '__main__':
    calculator = Calculator()
    calculator.run()