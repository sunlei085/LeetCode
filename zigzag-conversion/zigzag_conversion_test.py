#!/usr/bin/env python
# -*-coding:utf-8 -*-
import unittest

from zigzag_conversion import Solution


class TestTwoSum(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        result = sol.convert('PAYPALISHIRING', 2)
        self.assertEquals(result, 'PYAIHRNAPLSIIG')

    def test_2(self):
        sol = Solution()
        result = sol.convert('PAYPALISHIRING', 3)
        self.assertEquals(result, 'PAHNAPLSIIGYIR')

    def test_3(self):
        sol = Solution()
        result = sol.convert('PAYPALISHIRING', 4)
        self.assertEquals(result, 'PINALSIGYAHRPI')


if __name__ == '__main__':
    unittest.main()
