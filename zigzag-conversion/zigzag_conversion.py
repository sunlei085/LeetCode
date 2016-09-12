#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        题目的意思是把字符串上下上下走之字形状,然后按行输出,比如包含数字0~22的字符串, 给定行数为5,走之字形如下:

        现在要按行输出字符,即:0 8 16 1 7 9 15 17 2…….

        如果把以上的数字字符看做是字符在原数组的下标, 给定行数为n = 5, 可以发现以下规律:

        (1)第一行和最后一行下标间隔都是interval = n*2-2 = 8 ;

        (2)中间行的间隔是周期性的,第i行的间隔是: interval–2*i,  2*i,  interval–2*i, 2*i, interval–2*i, 2*i, …
        地址：http://www.cnblogs.com/TenosDoIt/p/3738693.html
        """
        if numRows <= 1:
            return s

        list_s = map(lambda x: x, s)
        list_result = list()
        for _ in xrange(numRows):
            flag = False
            # 第一行和最后一行下标间隔都是interval = n*2-2 = 8
            if _ == 0 or _ == numRows - 1:
                for i in xrange(_, len(list_s), numRows * 2 - 2):
                    list_result.append(list_s[i])
            # 中间行的间隔是周期性的,第i行的间隔是: interval–2*i,  2*i,  interval–2*i, 2*i, interval–2*i, 2*i,
            else:
                index = _
                while index < len(list_s):
                    if not flag:
                        list_result.append(list_s[index])
                        index += numRows * 2 - 2 - 2 * _
                        flag = True
                    else:
                        list_result.append(list_s[index])
                        index += 2 * _
                        flag = False

        return ''.join(list_result)
