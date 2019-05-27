import unittest

# Name: Euclidean Algorithm
# Runtime Analysis: O(N)


def gcd(num1: 'Integer', num2: 'Integer') -> 'Integer':
    """Returns the greatest common divisor of two integers"""
    if(num2 == 0):
        return num1
    else:
        remainder = num1 % num2
        return gcd(num2, remainder)


# Function Exists For User Verification Of Factors
def print_factors(num: "Integer") -> "Integer":
    """Helper function: returns all factors of any integer"""
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
    # print(f"Factors Of {num}: {factors}")


class Test(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(-86, 80), 2)
        self.assertEqual(gcd(-5, -25), -5)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(10, 20), 10)

    def test_print_factors(self):
        self.assertEqual(print_factors(54), [1, 2, 3, 6, 9, 18, 27, 54])
        self.assertEqual(print_factors(24), [1, 2, 3, 4, 6, 8, 12, 24])


if __name__ == "__main__":
    unittest.main()
