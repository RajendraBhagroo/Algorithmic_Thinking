"""
Link: https://leetcode.com/problems/two-sum/

Problem:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Input:
        nums = [2, 7, 11, 15]
        target = 9

    Output: 
        [0, 1]

    Explenation: 
        nums[0] + nums[1] = 2 + 7 = 9
"""
from typing import List
import unittest


class Solution:
    @staticmethod
    def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
        """Brute Force Solution.

        Time Complexity: 0(N^2)
            - Where N Is Length Of Array [nums]

        Space Complexity: 0(1)
        """
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return False

    @staticmethod
    def two_sum_hash_table(nums: List[int], target: int) -> List[int]:
        """Linear Time Solution.

        Time Complexity: 0(N) 
            - Where N Is Length Of Array [nums]

        Space Complexity: 0(N)
            - Where N Is Size Of HashTable 
        """
        hash_table = dict()
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i
        return False


class Test(unittest.TestCase):

    def test_two_sum_brute_force(self):
        self.assertEqual(
            Solution().two_sum_brute_force(
                [2, 7, 11, 15], 9
            ), [0, 1]
        )

        self.assertEqual(
            Solution().two_sum_brute_force(
                [2, 7, 11, 15], -1
            ), False
        )

        self.assertEqual(
            Solution().two_sum_brute_force(
                [-19, 50, 8, 2, 78, 51], 101
            ), [1, 5]
        )

    def test_two_sum_hash_table(self):
        self.assertEqual(
            Solution().two_sum_hash_table(
                [-6, -1, 2, 20, 9, 10, 1], 21
            ), [3, 6]
        )

        self.assertEqual(
            Solution().two_sum_hash_table(
                [-8, 6, 2, 18, 100, 11], 900
            ), False
        )


if __name__ == "__main__":
    unittest.main()
