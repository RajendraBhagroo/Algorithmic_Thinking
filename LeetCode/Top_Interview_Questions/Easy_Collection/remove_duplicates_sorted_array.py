"""
Link: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

Problem:
  Remove Duplicates from Sorted Array
  
  Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
  Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
  Input: nums = [1,1,2]
  Output: length = 2
    
    The first two elements of nums should be 1 and 2 respectively.
    It doesn't matter what you leave beyond the returned length.

Example 2:
  Input: nums = [0,0,1,1,1,2,2,3,3,4]
  Output: length = 5
    
    The first five elements of nums should be modified to 0, 1, 2, 3, and 4 respectively.
    It doesn't matter what values are set beyond the returned length.
"""
import unittest
from typing import List


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        """Removes duplicate elements in an array.

        Time Complexity: O(N) 
            - Where N Is Size Of Array [nums]

        Space Complexity: O(1)
        """

        # This Program Assumes Array Has Atleast 2 Elements
        if len(nums) <= 1:
            return len(nums)

        # If There Are Duplicates, Delete Them! Only Count Unique Numbers
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                del nums[i]
            else:
                i += 1
        return i


class Test(unittest.TestCase):

    def test_remove_duplicates(self):
        # Test Cases From Question
        self.assertEqual(Solution().remove_duplicates(
            [1, 1, 2]
        ), 2)

        self.assertEqual(Solution().remove_duplicates(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        ), 5)

        # Custom Test Cases
        self.assertEqual(Solution().remove_duplicates([]), 0)
        self.assertEqual(Solution().remove_duplicates([0]), 1)


if __name__ == "__main__":
    unittest.main()
