# -*- coding: utf-8 -*-s

import unittest

from add_two_nums import Solution


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TestAddTwoNums(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        list1 = ListNode(2)
        list1.next = ListNode(4)
        list1.next.next = ListNode(3)

        list2 = ListNode(5)
        list2.next = ListNode(6)
        list2.next.next = ListNode(4)

        result = sol.addTwoNumbers(list1, list2)

        list_result = list()
        while result:
            list_result.append(result.val)
            result = result.next

        self.assertEquals(list_result, [7, 0, 8])

        # def test_2(self):
        #     sol = Solution()
        #     result = sol.addTwoNumbers([2, 4, 3, 3], [5, 6, 4])
        #
        #     self.assertEquals(result, [7, 0, 8, 3])
