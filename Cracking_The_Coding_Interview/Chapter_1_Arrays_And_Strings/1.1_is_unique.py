"""
Problem:
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

Input:
    Any valid string

Output:
    Boolean [True | False] indicating if all characters within the input string are unqiue

Examples:
    Input: "abcdefghijklmnopqrstuvwxyz"
    Output: True
    
    Input: "racecar"
    Output: False
"""
import unittest


class Solution:

    @staticmethod
    def is_unique(input_string: str) -> bool:
        """Checks if any given string contains duplicate characters.

        Time Complexity: O(N)
            - Where N is length of string [input_string]

        Space Complexity: O(1)
            - Assuming ASCII 7 bit character set (2^7 = 128 characters)
            - Boolean array [known_characters] will always be fixed to accommodate character set
        """
        if len(input_string) > 128:
            return False

        known_characters = [False] * 128

        # For Each Characters ASCII Value [index], Set The Corresponding Array Value To True When First Encountered, Indicating That The Character Is Now Known
        # Return False If Any Character Is Already Known [Index Flag Already Set To True]
        for char in input_string:
            index = ord(char)
            if known_characters[index]:
                return False
            else:
                known_characters[index] = True
        return True


class Test(unittest.TestCase):

    def test_is_unique(self):
        # No Repeats
        self.assertEqual(Solution.is_unique(
            "abcdefghijklmnopqrstuvwxyz"), True)

        # Repeats
        self.assertEqual(Solution.is_unique(
            "racecar"), False)

        # String Of Length 0
        self.assertEqual(Solution.is_unique(
            ""), True)

        # Multiple Spaces
        self.assertEqual(Solution.is_unique(
            " h j "), False)

        # Longer Than 128 Chacters
        self.assertEqual(Solution.is_unique(
            "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), False)


if __name__ == "__main__":
    unittest.main()
