"""
Problem:
    Write a method to replace all spaces in a string with "%20". 
    You may assume the that the string has sufficient space at the end to hold the additional characters,
    and that you are given the "true" length of the string.

Example:
    Input: "Mr John Smith    ", 13
    Output: "Mr%20John%20Smith"
"""
import unittest


class Solution:

    @staticmethod
    def URLify(url: str, length: int = None) -> str:
        """Converts spaces in [url] to be URL safe.

        Time Complexity: O(N)
            - Where N is length of string [url]

        Space Complexity:
            - 0(1)
        """

        # This Is The Code From The Booksite, I Found Out It Only Works For Trailing Whitespaces!
        #
        # Booksite Code
        # See: https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter1/3_URLify/URLify.py
        #      [Line 6] -> Only Works For Trailing Whitespaces. Valid URL's Also Need Leading Whitespace Removed
        #
        # Github User
        # See: https://github.com/Turingfly/cracking-the-coding-interview/blob/master/src/chapter01ArraysAndStrings/Urlify.java
        #      [Line 41] -> This User Has Identified My Concerns And Included ".trim()" In Their Returned String To Account For Leading Whitespace
        """
        # Python Strings Are Immutable, So I Used A List To Avoid Unnecessary String Objects
        url = list(url)
        new_index = len(url)

        for i in reversed(range(length)):
            if url[i] == ' ':
                # Replace spaces
                url[new_index - 3:new_index] = '%20'
                new_index -= 3
            else:
                # Move characters
                url[new_index - 1] = url[i]
                new_index -= 1

        return "".join(url)
        """

        # Here Is My Condensed Code That Works For Leading/Trailing Whitespaces
        # Alternatively You Can Manually Loop Through Each Character Or Use Regex
        # To Remove Leading/Trailing Whitespaces & Preserve "%20" Rule, However Builtins In This Case Are More Efficient
        return url.strip().replace(" ", "%20")


class Test(unittest.TestCase):

    def test_URLify(self):
        self.assertEqual(Solution.URLify(
            "Mr John Smith    ", 13), "Mr%20John%20Smith")
        self.assertEqual(Solution.URLify(
            "     Mr Rajendra Bhagroo    ", 19), "Mr%20Rajendra%20Bhagroo")


if __name__ == "__main__":
    unittest.main()
