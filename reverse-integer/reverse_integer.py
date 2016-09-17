#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        本题没有使用python语言的强制类型转换，考虑到强制类型转换就没有什么意义了对于该题，所以还是使用了算法，
        不过看网上的算法都是不这个牛逼，这个算是最土的了
        while x:
            result = result * 10 + x % 10
            x /= 10
        这种方法比较酷，x%10这个取余数即刚好是最后一位，x/10这个是地板除缩短一位。巧妙刚好用到反转过来了，最小的变成最大的了。
        这个解题方法真是妙极了
        """
        flag = -1 if x != abs(x) else 1

        x = abs(x)
        str_int = str(x)
        list_x = list()
        len_input_num = len(str_int)

        for _ in xrange(len_input_num):
            divisor_num = 10 ** (len(str_int) - _ - 1)
            list_x.append(x / divisor_num)
            x -= list_x[-1] * divisor_num

        list_x.reverse()
        result = 0

        for index, _ in enumerate(list_x):
            result += _ * 10 ** (len_input_num - 1 - index)

        # 题目要求integer是32位整型，考虑溢出，结果大于32位整形的话就要考虑溢出返回值为0
        if result > (2 ** 31 - 1):
            return 0

        return flag * result


print Solution().reverse(1534236469)
