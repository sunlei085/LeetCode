# -*-coding:utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    不能删除注释class ListNode这个类，应该是用于测试的不能修改，若去掉后在LeetCode上会报错误
    """

    def addTwoNumbers(self, l1, l2):
        nHead, flag = ListNode(0), 0
        head = nHead
        while flag or l1 or l2:
            node = ListNode(flag)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            flag = node.val // 10
            node.val %= 10
            # 这句很重要，next指定为下个类实例。同时指针需要往后移动
            head.next, head = node, node
        # 这句也很关键必须要是next因为第一个初始化时为0，从下一个开始
        return nHead.next
