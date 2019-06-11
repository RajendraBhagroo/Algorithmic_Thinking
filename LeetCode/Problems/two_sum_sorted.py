"""
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem:
    Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

    Note:
        Your returned answers (both index1 and index2) are not zero-based.
        You may assume that each input would have exactly one solution and you may not use the same element twice.
    
Example:
    Input: 
        numbers = [2,7,11,15]
        target = 9

    Output:
        [1,2]
    
    Explanation: 
        The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
from typing import List
import unittest


class Solution:
    @staticmethod
    def two_sum_sorted(nums: List[int], target: int) -> List[int]:
        """Returns List Of Indices Contianing Solution [See Problem Example].

        Assuming List Is Sorted

        Time Complexity: 0(N) 
            - Where N Is Length Of Array [nums]

        Space Complexity: 0(1)
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return False


class Test(unittest.TestCase):

    def test_two_sum_sorted(self):
        self.assertEqual(Solution().two_sum_sorted([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution().two_sum_sorted([2, 7, 11, 15], -1), False)


if __name__ == "__main__":
    unittest.main()
