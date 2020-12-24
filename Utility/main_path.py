# _*_ coding: utf-8 _*_
# _author_ = 'zdq'

import os


# 获取项目路径（通过当前文件路径拼接项目路径）
def get_obj_path():
    # 当前系统分隔符
    sep = os.path.sep
    # 获取当前文件路径
    current_path = os.path.abspath(os.path.dirname(__file__))
    # 获取项目的根路径
    paths = current_path.replace('/', sep).split(sep)
    object_path = sep.join(paths[:len(paths)-1])
    return object_path
