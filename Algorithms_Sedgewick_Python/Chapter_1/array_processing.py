from array import array
import unittest

# Array Processing


def arr_max(array_: "Array: Integers") -> "Integer: Max Element In Array":
    """Find The Maximum Value Within An Array"""
    max_element = array_[0]
    for element in array_:
        if(element > max_element):
            max_element = element
    return max_element


def arr_avg(array_: "Array: Floats") -> "Float: Average Rounded To 2 Decimal Digits":
    """Compute The Average Of Array Values"""
    sum = 0.0
    for element in array_:
        sum += element
    average = sum / len(array_)
    return round(average, 2)


def arr_copy(array_: "Array: Integers") -> "Array: Replicated Array Of Integers":
    """Copy Elements Of One Array To A New Array"""
    copy = array('i', [0] * len(array_))
    i = 0
    while (i < len(array_)):
        copy[i] = array_[i]
        i += 1
    return copy


def arr_reverse(array_: "Array: Integers") -> "Array: Reversed Original Array":
    """Reverse Elements Within Array"""
    start = len(array_)
    end = 0
    while (start < end):
        array_[start], array_[end] = array_[end], array_[start]
        start += 1
        end -= 1
    return array_


def arr_maxtrix_multiplication(array_1: "Matrix", array_2: "Matrix") -> "Matrix":
    """
    Matrix-Matrix Multiplication (Square Matrices)

    Input: 3x3 matrix
    array_1 = [[12,7,3],
               [4 ,5,6],
               [7 ,8,9]]

    Input: 3x4 matrix
    array_2 = [[5,8,1,2],
               [6,7,3,0],
               [4,5,9,1]]

    Output: 3x4 Matrix
    result = [[114, 160, 60, 27],
              [74, 97, 73, 14],
              [119, 157, 112, 23]]
    """
    result = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    # Iterate Through Rows Of Array 1
    for i in range(len(array_1)):
        # iterate through columns of Array 2
        for j in range(len(array_2[0])):
            # iterate through rows of Array 2
            for k in range(len(array_2)):
                result[i][j] += array_1[i][k] * array_2[k][j]
    return result


class Test(unittest.TestCase):

    def test_arr_max(self):
        self.assertEqual(
            arr_max(
                array('i', [10, 3, 9, 12, 8])
            ), 12)

    def test_arr_avg(self):
        self.assertEqual(
            arr_avg(
                array('f', [1.2, 13.56, 8.9])
            ), 7.89)
        self.assertNotEqual(
            arr_avg(
                array('f', [1.2, 13.56, 8.9])
            ), 7.886)

    def test_arr_copy(self):
        self.assertEqual(
            arr_copy(
                array('i', [7, 4, 10, 6])
            ), array('i', [7, 4, 10, 6]))
        self.assertNotEqual(
            arr_copy(
                array('i', [1, 2, 3])
            ), array('i', [1, 2]))

    def test_arr_reverse(self):
        self.assertNotEqual(
            arr_reverse(
                array('i', list(range(1, 11)))
            ),
            array('i', list(range(10, 0, -1))))

    def test_arr_maxtrix_multiplication(self):
        self.assertEqual(
            arr_maxtrix_multiplication(
                array_1=[[12, 7, 3],
                         [4, 5, 6],
                         [7, 8, 9]],
                array_2=[[5, 8, 1, 2],
                         [6, 7, 3, 0],
                         [4, 5, 9, 1]]
            ),
            [[114, 160, 60, 27],
             [74, 97, 73, 14],
             [119, 157, 112, 23]]
        )


if __name__ == "__main__":
    unittest.main()
