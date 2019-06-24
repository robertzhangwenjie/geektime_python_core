#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/5/23 6:50
# @Author   :   robert
# @FileName :   word_counter.py
# @Software :   PyCharm



# 统计大段文本中的每个单词的个数,按照从高到低排序返回
import re
from collections import defaultdict


class WordCounter(object):
    # 统计大段文本文件中的词频
    def word_count(self,file):
        # 初始化一个默认值为0字典
        word_dic = defaultdict(int)

        try:
            with open(file,'r') as f:
                # 循环读取每一行
                for text in f:
                    # 去掉标点符号或者换行符等非单词
                    text = re.sub(r'[^0-9a-zA-Z]',' ',text)

                    # 转换为小写
                    text = text.lower()

                    # 将文本用空格分割成一个单词列表
                    word_list = text.split(' ')
                    # 去掉单词列表中的空对象，如可能有空格
                    word_list = filter(lambda x:x,word_list)

                    # 统计每个单词出现的频率
                    for word in word_list:
                        word_dic[word] += 1

            # 对词频进行排序
            word_sorted_tuple = sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
            return word_sorted_tuple
        except Exception as e:
            raise e


if __name__ == '__main__':
    word_counter = WordCounter()
    word_count = word_counter.word_count('./testfile')
    try:
        with open('word_count.txt','w') as f:
            for k,v in word_count:
                f.write('{}:{}\n'.format(k,v))
    except Exception as e:
        print(e)
        print('writing error')
