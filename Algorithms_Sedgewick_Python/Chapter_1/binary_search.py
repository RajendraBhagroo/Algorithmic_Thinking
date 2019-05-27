import unittest

# Lists MUST Be Sorted Prior To Use


# Name: Binary Search [Iterative]
# Runtime Analysis: O(Log N)
def binary_search_iterative(list_: "List Of Integers", key: "Value To Find Within List") -> "Index Of Value Within List If Exists, Or -1":
    """
    Searches For Key Within List.
    If The Search Is Successful, The Algorithm Will Return The Index Where The Key Was Found Within The List.
    Otherwise It Will Return -1 For Not Found.
    """
    low = 0
    high = len(list_) - 1
    while (low <= high):
        mid = low + (high - low) // 2
        if (key < list_[mid]):
            high = mid - 1
        elif(key > list_[mid]):
            low = mid + 1
        else:
            return mid
    return -1


# Name: Binary Search [Recursive]
# Runtime Analysis [Stack Space]: T(N) = T(N-2) + c
# Runtime Analysis: O(Log N)
def binary_search_recursive(list_: "List Of Integers", key: "Value To Find Within List") -> "Index Of Value Within List If Exists, Or -1":
    """
    Searches For Key Within List.
    If The Search Is Successful, The Algorithm Will Return The Index Where The Key Was Found Within The List.
    Otherwise It Will Return -1 For Not Found.
    """
    return _binary_search_recursive(list_, key, 0, len(list_) - 1)


# Private Function [Weak Convention]
def _binary_search_recursive(
    list_: "List Of Integers",
    key: "Value To Find Within List",
    low: "Current Lower Search Bound",
    high: "Current UpperSearch  Bound"
)-> "Index Of Value Within List If Exists, Or -1":
    """Private Function Used To Maintain Transparency Of Binary Search To Caller"""
    if(low > high):
        return -1

    mid = low + (high - low) // 2

    if(key < list_[mid]):
        return _binary_search_recursive(list_, key, low, mid - 1)
    elif(key > list_[mid]):
        return _binary_search_recursive(list_, key, mid + 1, high)
    else:
        return mid


class Test(unittest.TestCase):

    def test_binary_search_iterative(self):
        self.assertEqual(
            binary_search_iterative(
                [3, 6, 10, 13, 17, 28], 17
            ), 4)
        self.assertEqual(
            binary_search_iterative(
                [3, 6, 10, 13, 17, 28], 12
            ), -1)

    # Same Test Case To Prove Transparency Between Iterative & Recursive
    def test_binary_search_recursive(self):
        self.assertEqual(
            binary_search_iterative(
                [3, 6, 10, 13, 17, 28], 17
            ), 4)
        self.assertEqual(
            binary_search_iterative(
                [3, 6, 10, 13, 17, 28], 12
            ), -1)


if __name__ == "__main__":
    unittest.main()
