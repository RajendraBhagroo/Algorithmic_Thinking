"""
Problem:
    Implement a function which removes all the even elements from a given list

Input:
    A list with random integers

Output:
    A list with only odd integers

Sample Input:
    myList = [1,2,4,5,10,6,3]

Sample Output:
    myList = [1,5,3]
"""
import unittest
from typing import List


class Solution:

    @staticmethod
    def remove_even(List_: List[int]) -> List[int]:
        """Removes all even integers in original list.

        Time Complexity: 0(N)
            - Where N is length of list [List_]

        Space Complexity: 0(1)
        """

        i = 0
        while i < len(List_):
            if List_[i] % 2 == 0:
                del List_[i]
            else:
                i = i + 1
        return List_

    # Alternate Solution
    @staticmethod
    def remove_even_comp(List: List[int]) -> List[int]:
        """Removes all even integers in original list.

        Time Complexity: 0(N)
            - Where N is length of list [List]

        Space Complexity: 0(1)
        """

        return [item for item in List if item % 2 != 0]


class Test(unittest.TestCase):

    def test_remove_even(self):
        self.assertEqual(Solution.remove_even(
            [1, 2, 4, 5, 10, 6, 3]), [1, 5, 3])

        self.assertEqual(Solution.remove_even(
            [-4, 102, -46, -16, 170, 19, 132, -161, 13, 125, 172, 25, -139, 16, -165, -108, 126, 30, 88, 151, 11, 54, -94, 60, 15, 68, -118, 63, 173, -142, 146, -97, -77, 113]), [19, -161, 13, 125, 25, -139, -165, 151, 11, 15, 63, 173, -97, -77, 113])

    def test_remove_even_comp(self):
        self.assertEqual(Solution.remove_even_comp(
            [1, 2, 4, 5, 10, 6, 3]), [1, 5, 3])

        self.assertEqual(Solution.remove_even_comp(
            [-4, 102, -46, -16, 170, 19, 132, -161, 13, 125, 172, 25, -139, 16, -165, -108, 126, 30, 88, 151, 11, 54, -94, 60, 15, 68, -118, 63, 173, -142, 146, -97, -77, 113]), [19, -161, 13, 125, 25, -139, -165, 151, 11, 15, 63, 173, -97, -77, 113])


if __name__ == "__main__":
    unittest.main()
