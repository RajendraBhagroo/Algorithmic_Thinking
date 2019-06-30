"""
Problem:
    In this problem, you have to implement the findSum(lst,value) function which will take a number n as input and return two numbers that add up to n

Input:
    A list and a number n

Output:
    A list with two integers a and b that add up to n

Sample Input:
    lst = [1,21,3,14,5,60,7,6]
    n = 81

Sample Output:
    lst = [21,60]
"""
import unittest
from typing import List


class Solution:

    @staticmethod
    def find_sum_brute(lst: List[int], value: int) -> int:
        """Returns A list containing two numbers whose sum equals [value].

        Time Complexity: O(N^2)
            - Where [N] is length of list [lst]

        Space Complexity: O(1)
        """
        for i in range(len(lst)):
            for j in range(len(lst)):
                if(lst[i]+lst[j] == value and i != j):
                    return [lst[i], lst[j]]

    # Search Introduces O(log(N)) Time Complexity
    @staticmethod
    def binarySearch(lst, item):
        first = 0
        last = len(lst) - 1
        found = False
        while first <= last and not found:
            mid = (first + last) // 2
            if lst[mid] == item:
                found = mid
            else:
                if item < lst[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return found

    @staticmethod
    def find_sum_sorted_complement(lst: List[int], value: int) -> int:
        """Returns A list containing two numbers whose sum equals [value].

        Time Complexity: O(N * Log(N))
            - Where [N] is length of array [lst]
            - Python uses TimSort from [.sort()] which is O(N * Log(N))
            - Binary Search incurs O(Log(N)) time complexity

        Space Complexity: O(1)
        """
        lst.sort()
        for num in lst:
            complement = Solution.binarySearch(lst, value-num)
            if complement:
                return [num, value-num]

    @staticmethod
    def find_sum_sorted_slider(lst: List[int], value: int) -> int:
        """Returns A list containing two numbers whose sum equals [value].

        Time Complexity: O(N * Log(N))
            - Where [N] is length of array [lst]
            - Python uses TimSort from [.sort()] which is O(N * Log(N))
            - Binary Search incurs O(Log(N)) time complexity

        Space Complexity: O(1)
        """
        lst.sort()
        index1 = 0
        index2 = len(lst) - 1
        result = []
        sum = 0

        while (index1 != index2):
            sum = lst[index1] + lst[index2]
            if sum < value:
                index1 += 1
            elif sum > value:
                index2 -= 1
            else:
                result.append(lst[index1])
                result.append(lst[index2])
                return result
        return False

    @staticmethod
    def find_sum_hash_table(lst: List[int], value: int) -> int:
        """Returns A list containing two numbers whose sum equals [value].

        Time Complexity: 0(N) 
            - Where [N] is length of array [lst]

        Space Complexity: 0(N)
            - Where [N] is size of hash table [foundValues]
        """
        foundValues = {}

        for ele in lst:
            try:
                foundValues[value - ele]
                return [value - ele, ele]
            except:
                foundValues[ele] = 0
        return False

    @staticmethod
    def find_sum_set(lst: List[int], value: int) -> int:
        """Returns A list containing two numbers whose sum equals [value].

        Time Complexity: 0(N) 
            - Where [N] is length of array [lst]

        Space Complexity: 0(N)
            - Where [N] is size of set [foundValues]
        """
        foundValues = set()
        for ele in lst:
            if value - ele in foundValues:
                return [value-ele, ele]
            foundValues.add(ele)
        return False


class Test(unittest.TestCase):

    def test_find_sum_brute(self):
        self.assertEqual(Solution.find_sum_brute(
            [1, 21, 3, 14, 5, 60, 7, 6], 81
        ), [21, 60])

    def test_find_sum_sorted_complement(self):
        self.assertEqual(Solution.find_sum_sorted_complement(
            [1, 21, 3, 14, 5, 60, 7, 6], 81
        ), [21, 60])

    def test_find_sum_sorted_slider(self):
        self.assertEqual(Solution.find_sum_sorted_slider(
            [1, 21, 3, 14, 5, 60, 7, 6], 81
        ), [21, 60])

    def test_find_sum_hash_table(self):
        self.assertEqual(Solution.find_sum_hash_table(
            [1, 21, 3, 14, 5, 60, 7, 6], 81
        ), [21, 60])

    def test_find_sum_set(self):
        self.assertEqual(Solution.find_sum_set(
            [1, 21, 3, 14, 5, 60, 7, 6], 81
        ), [21, 60])


if __name__ == "__main__":
    unittest.main()
