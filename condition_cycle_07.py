#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/25 7:36
# @Author   :   robert
# @FileName :   condition_cycle_07.py
# @Software :   PyCharm



l_color =dict()

l_price = dict()

# 1.价格小于1000，并且颜色不是红色的所有产品名称和颜色的组合
ret = dict()
for pro,price in l_price.items():
    if price >= 1000:
        continue
    elif pro not in l_price:
        continue
    elif l_price[pro] == 'red':
        continue
    else:
        ret[pro] = l_price[pro]
    print(ret)

# 2.求 y= |x| + 5

def f(x):
    ret = x + 5 if x > 0 else -x + 5
    return ret

li = [1,2,-2,3]
ret = [x if x>0 else -x for x in li]
# 等价于 for x in li:
#            if x >0:
#                return x
#            else:
#                return -x



# 3.将文件中逐行读取的一个完整语句，按逗号分割单词，
# 去掉收尾空字符串，并过滤掉长度小于等于3的单词返回一个列表

s = ' Today, is, sunday'
rets = [i.strip() for i in s.split(',') if len(i.strip()) >3]


# 4.给定两个列表x,y 要求返回x,y中所有元素对组成的元组的列表，相等情况除外
x = [1,2,3,4,5]
y = [3,6,7,8]

ret_t = [(xx,yy) for xx in x for yy in y if xx != yy]

# 5.给定两个列表attributes 和 values，要求针对values中每一组子列表value，输出
# 其和attributes中的键对应后的字典，最后范湖字典组成的列表
attributes = ['name','dob','age']
values = [['robert','1990-08-09',29],
          ['john','1983-07-09',36],
          ['jack','1990-04-05',29]
          ]
ret_av = [dict(zip(attributes,value))for value in values]
print(ret_av)
