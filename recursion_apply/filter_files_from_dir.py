#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time     :   2019/6/24 21:15
# @Author   :   robert
# @FileName :   filter_files_from_dir.py
# @Software :   PyCharm
import os

def get_files(file_path,suffix):
    '''
    采用闭包中局部变量的方式，递归文件夹中的所有文件，然后增加到list
    :param file_path: 文件夹路径
    :param suffix: 要找的文件后缀
    :return: 文件名列表
    '''
    files_list = []
    def filter_file(file_path :str):
        if os.path.isdir(file_path):
            files = os.listdir(file_path)
            for file_name in files:
                file = os.path.join(file_path,file_name)
                filter_file(file)

        if file_path.endswith(suffix):
            files_list.append(file_path)
        return files_list
    return filter_file(file_path)

def get_jars(file_path :str):
    '''
    获取文件夹中的所有jar文件
    思路: 递归文件夹，如果是文件则直接添加到files_list,并返回
          如果是文件夹，则需要将文件夹中的所有的子文件或者子文
                件夹的返回值添加到这个文件夹列表jars_list
    要点: 文件夹需要返回所有文件的list
          函数的返回值
    :param file_path: 文件路径
    :return:
    '''
    files_list = []
    # 如果是文件夹，则需要返回文件夹中的所有jars
    if os.path.isdir(file_path):
        files = os.listdir(file_path)
        # 用来返回文件夹中的所有jar包
        jars_list = []
        for file_name in files:
            file = os.path.join(file_path,file_name)
            # 获取每个子文件或文件夹的jars，然后添加到jars_list
            jars_list.extend(get_jars(file))
        # 返回文件夹中的所有jars
        return jars_list
    # 当文件为.jar结尾时直接返回该jar文件的列表
    if file_path.endswith(".jar"):
        files_list.append(file_path)
    return files_list



if __name__ == '__main__':
    file_path = "D:\maven_repo"
    res = get_jars(file_path)
    print(len(res))

