# -*- coding: utf-8 -*-s

import unittest

from twosum import Solution


class TestTwoSum(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [3, 2, 4]
        target = 6
        result = sol.twoSum(nums, target)
        self.assertEquals(result, [1, 2])


if __name__ == '__main__':
    unittest.main()
