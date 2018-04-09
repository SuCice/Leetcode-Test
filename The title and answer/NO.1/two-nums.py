# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 下午9:38
# @Author  : suchao
# @Email   : mat_wu@163.com
# @File    : two-nums.py
# @Software: PyCharm
#
class Findindex (object):
    def twoNums(self,nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i
