#!/usr/bin/env python
# -*-coding:utf-8 -*-

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        input_str = str.strip()
        if not input_str:
            return 0

        # if判断老搞错，这个是逻辑思维得有多差啊
        if (input_str[0] < '0' or input_str[0] > '9') and (input_str[0] != '+' and input_str[0] != '-'):
            return 0

        flag = -1 if input_str[0] == '-' else 1

        list_output = list()
        if input_str[0] == '-' or input_str[0] == '+':
            for index, _ in enumerate(input_str):
                if index != 0 and (_ >= '0' and '9' >= _):
                    list_output.append(_)
                elif index != 0:
                    break
        else:
            for _ in input_str:
                if _ >= '0' and '9' >= _:
                    list_output.append(_)
                else:
                    break

        result = 0

        for index, _ in enumerate(list_output):
            result += int(_) * 10 ** (len(list_output) - 1 - index)

        # 题目要求integer是32位整型，考虑溢出，结果大于32位整形的话就考虑返回最大值，小于最小值就返回最小值，我也是醉了
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if flag * result > INT_MAX:
            return INT_MAX
        elif flag * result < INT_MIN:
            return INT_MIN
        else:
            return flag * result


print Solution().myAtoi("-2147483648")
