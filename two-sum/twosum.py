# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            for index_j, num_j in enumerate(nums[index + 1:]):
                if num + num_j == target:
                    return [index, index_j + index + 1]
