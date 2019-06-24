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
    # 统计字符串文本的词频
    def word_count(self,text):
        # 去掉标点符号或者换行符等非单词
        text = re.sub(r'[^0-9a-zA-Z]',' ',text)

        # 转换为小写
        text = text.lower()

        # 将文本用空格分割成一个单词列表
        word_list = text.split(' ')
        # 去掉单词列表中的空对象，如可能有空格
        word_list = filter(lambda x:x,word_list)

        # 初始化一个默认值为0字典
        word_dic = defaultdict(int)
        # 统计每个单词出现的频率
        for word in word_list:
            word_dic[word] += 1

        # 对词频进行排序
        # word_sorted_tuple = sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
        # return word_sorted_tuple

        return word_dic

    def count(self,file):
        '''
        统计文件中的单词出现的频率
        :param file:
        :return:
        '''
        word_cnt = defaultdict(int)
        try:
            with open(file,'r') as f:
                # 读取文件的每一行，然后将每一行的统计和之前的统计相加
                for line in f:
                    _word_cnt = self.word_count(line)
                    for word,cnt in _word_cnt.items():
                        word_cnt[word] += _word_cnt[word]

            word_cnt = sorted(word_cnt.items(),key=lambda x:x[1],reverse=True)
            return word_cnt
        except Exception as e:
            print(e)
            print('count error')
if __name__ == '__main__':
    word_counter = WordCounter()
    word_count = word_counter.count('./testfile')
    try:
        with open('word_count.txt','w') as f:
            for k,v in word_count:
                f.write('{}:{}\n'.format(k,v))
    except Exception as e:
        print(e)
        print('writing error')
