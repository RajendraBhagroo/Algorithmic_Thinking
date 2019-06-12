"""
Problem:
    Implement a function which merges two sorted lists into another sorted list. Name it merge_lists(lst1, lst2)

Input:
    Two sorted lists

Output:
    A merged and sorted list consisting of all elements of both input lists

Sample Input:
    arr1 = [1,3,4,5]
    arr2 = [2,6,7,8]

Sample Output:
    arr = [1,2,3,4,5,6,7,8]
"""
import unittest
from typing import List


class Solution:

    @staticmethod
    def merge_sorted_lists(lst1: List[int], lst2: List[int]) -> List[int]:
        """Merge Two Sorted Lists.

        Time Complexity: O(m(n+m))
            - Where [n] is length of [lst1]
            - Where [m] is length of [lst2]
            - Insert Operation Is 0(n), Occurs [m] Times In Worst Case

        Space Complexity: O(m)
        """
        i = 0
        j = 0
        while(i < len(lst1) and j < len(lst2)):
            if(lst1[i] > lst2[j]):
                lst1.insert(i, lst2[j])
                i += 1
                j += 1
            else:
                i += 1

        # Add Remaining Elements To [lst1]
        if(j < len(lst2)):
            lst1.extend(lst2[j:])
        return lst1

    @staticmethod
    def merge_sorted_lists_alt(lst1: List[int], lst2: List[int]) -> List[int]:
        """Merge Two Sorted Lists.

        Time Complexity: O(m + n)
            - Where [n] is length of [lst1]
            - Where [m] is length of [lst2]

        Space Complexity: O(m + n)
        """
        lst3 = [None] * (len(lst1) + len(lst2))
        i = 0
        j = 0
        k = 0

        # Loop Through Both Lists Once
        while i < len(lst1) and j < len(lst2):

            # Compare Elements In [lst1] and [lst2]
            # Add Smaller Of The Two Into [lst3]
            if lst1[i] < lst2[j]:
                lst3[k] = lst1[i]
                k = k + 1
                i = i + 1

            else:
                lst3[k] = lst2[j]
                k = k + 1
                j = j + 1

        # Add Remaining Elements Of [lst1] To [lst3]
        while i < len(lst1):
            lst3[k] = lst1[i]
            k = k + 1
            i = i + 1

        # Add Remaining Elements Of [lst2] To [lst3]
        while j < len(lst2):
            lst3[k] = lst2[j]
            k = k + 1
            j = j + 1

        return lst3


class Test(unittest.TestCase):
    def test_merge_sorted_lists(self):
        self.assertEqual(Solution.merge_sorted_lists([], []), [])

        self.assertEqual(Solution.merge_sorted_lists(
            [1, 3, 4, 5],
            [2, 6, 7, 8]),
            [1, 2, 3, 4, 5, 6, 7, 8]
        )

        self.assertEqual(Solution.merge_sorted_lists(
            [],
            [1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5]
        )

        self.assertEqual(Solution.merge_sorted_lists(
            [1, 4, 45, 63],
            []),
            [1, 4, 45, 63]
        )

        self.assertEqual(Solution.merge_sorted_lists(
            [-133, -100, 0, 4],
            [-2000, 2000]),
            [-2000, -133, -100, 0, 4, 2000]
        )

    # Running Same Test Cases For Both Methods
    def test_merge_sorted_lists_alt(self):
        self.assertEqual(Solution.merge_sorted_lists_alt([], []), [])

        self.assertEqual(Solution.merge_sorted_lists_alt(
            [1, 3, 4, 5],
            [2, 6, 7, 8]),
            [1, 2, 3, 4, 5, 6, 7, 8]
        )

        self.assertEqual(Solution.merge_sorted_lists_alt(
            [],
            [1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5]
        )

        self.assertEqual(Solution.merge_sorted_lists_alt(
            [1, 4, 45, 63],
            []),
            [1, 4, 45, 63]
        )

        self.assertEqual(Solution.merge_sorted_lists_alt(
            [-133, -100, 0, 4],
            [-2000, 2000]),
            [-2000, -133, -100, 0, 4, 2000]
        )


if __name__ == "__main__":
    unittest.main()
