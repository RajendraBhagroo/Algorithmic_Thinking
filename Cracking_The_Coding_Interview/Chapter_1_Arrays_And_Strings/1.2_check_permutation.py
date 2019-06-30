"""
Problem:
    Given two strings, write a method to decide if one is a permutation of the other.

Input:
    str1 -> String to check if permutation exists
    str2 -> String which represents potential permutation of str1

Output:
    Boolean [True | False] indicating if [str2] is a valid permutation of [str1]

Examples:
    Input:
        str1 = "ABC"
        str2 = "BAC"
    Output:
        True 
    
    Input: 
        str1 = "1234"
        str2 = "4358"
    Output:
        False 
"""
import unittest
from collections import Counter


class Solution:

    @staticmethod
    def check_permutation(str1, str2: str) -> bool:
        """Checks if [str2] is a valid permutation of [str1].

        Time Complexity: O(N)
            - Where N is the length of string [str1]

        Space Complexity: O(1)
            - Auxiliary space upper bound would be length of characterset
            - This example assumes ASCII characterset, could be unicode!
        """
        # By Definition, Permutations Must Be Equal Length
        if len(str1) != len(str2):
            return False

        # See: https://docs.python.org/3.7/library/collections.html#collections.Counter
        counter = Counter()

        # Increment Character Count For Each Character Processed In [str1]
        for char in str1:
            counter[ord(char)] += 1

        # Decrement Character Count For Each Character Processed In [str2]
        # All Character Counts Must Tally To 0 For A Valid Permutation. [str1 And str2 Must Have Same Number Of Characters]
        # Return False If Any Character Count Is Negative, Or There Is A New Character In [str2] Not Seen In [str1]. [Counter Class Sets New Element To 0]
        for char in str2:
            if counter[ord(char)] == 0:
                return False
            counter[ord(char)] -= 1
        return True


class Test(unittest.TestCase):

    def test_check_permutation(self):
        self.assertEqual(Solution.check_permutation("ABC", "BAC"), True)
        self.assertEqual(Solution.check_permutation("", ""), True)
        self.assertEqual(Solution.check_permutation("A ", " A"), True)
        self.assertEqual(Solution.check_permutation("1234", "4358"), False)

        # Case Sensitive
        self.assertEqual(Solution.check_permutation("Hello", "elloh"), False)

        # Whitespace Sensitive
        self.assertEqual(Solution.check_permutation(
            "Hello ", " Hello  "), False)


if __name__ == "__main__":
    unittest.main()
