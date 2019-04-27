"""
Link: https://leetcode.com/problems/reverse-integer/

Problem: 
    Given a 32-bit signed integer, reverse digits of an integer.

    Note:
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21
"""
import unittest


class Solution:
    @staticmethod
    def reversed_integer(x: int) -> int:
        """Reverses integer passed to function, based on order not negation.

        Time Complexity: 0(N) Where N Is Size Of Array
        Space Complexity: 0(N) Where N Is Size Of Solution List
        """

        # Handles Integer Overflow & Underflow For Input
        if x > (2**31)-1 or x < (-2)**31:
            return 0

        solution = []

        # Handles Negative Numbers [Example 2]
        if x < 0:
            solution.append("-")

        x = str(x)

        # Reverse Input Using List, Strings Are Immutable [Also Ignores Negative Sign For Consistency]
        for i in range(len(x) - 1, -1, -1):
            if x[i] == "-":
                continue
            solution.append(x[i])

        # Remove Leading 0's [Example 3]
        if solution[0] == '0':
            solution = solution[0:]

        solution = int(''.join(solution))

        # Handles Integer Overflow & Underflow For Solution [Reversed Integer]
        if solution > (2**31)-1 or solution < (-2)**31:
            return 0

        return solution


class Test(unittest.TestCase):

    def test_reversed_integer(self):
        # Out Of Range
        self.assertEqual(Solution().reversed_integer(2 ** 32), 0)
        self.assertEqual(Solution().reversed_integer(-2 ** 32), 0)
        self.assertEqual(Solution().reversed_integer(1534236469), 0)

        # See Examples
        self.assertEqual(Solution().reversed_integer(123), 321)
        self.assertEqual(Solution().reversed_integer(1036500), 56301)
        self.assertEqual(Solution().reversed_integer(-435532), -235534)


if __name__ == "__main__":
    unittest.main()
