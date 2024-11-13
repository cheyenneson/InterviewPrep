def bitwise_and_of_range(m: int, n: int) -> int:
    """
    Problem 1: Bitwise AND of Numbers Range
    Given two integers m and n, return the bitwise AND of all the numbers in the range [m, n], inclusive.
    """
    result = m
    for i in range(m + 1, n + 1):
        result &= i
    return result

def single_number(nums: list[int]) -> int:
    """
    Problem 2: Single Number II
    Given a list of integers, every element appears three times except for one. Find that single one which appears exactly once.
    """
    pass

def count_total_set_bits(n: int) -> int:
    """
    Problem 3: Count Total Set Bits
    Given a positive integer n, count the total number of set bits (1s) in binary representation of all numbers from 1 to n.
    """
    pass

def reverse_bits(x: int) -> int:
    """
    Problem 4: Reverse Bits
    Given a 32-bit unsigned integer, reverse its bits and return the resulting integer.
    """
    pass

def maximum_xor(nums: list[int]) -> int:
    """
    Problem 5: Maximum XOR of Two Numbers in an Array
    Given a non-empty array of numbers, find the maximum result of a pair of numbers' XOR in that array.
    """
    pass

def smallest_power_of_two_greater_than_or_equal(x: int) -> int:
    """
    Problem 6: Smallest Power of Two Greater than or Equal to n
    Given an integer x, find the smallest power of 2 greater than or equal to x.
    """
    pass

def bit_difference(a: int, b: int) -> int:
    """
    Problem 7: Bit Difference
    Given two integers a and b, return the number of bits that need to be flipped to convert a to b.
    """
    pass

def hamming_weight(n: int) -> int:
    """
    Problem 8: Hamming Weight
    Given an unsigned integer n, return the number of '1' bits it has (also known as the population count).
    """
    pass

def swap_odd_even_bits(n: int) -> int:
    """
    Problem 9: Swap Odd and Even Bits
    Given an unsigned integer n, swap all odd bits with even bits. (For example, bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on.)
    """
    pass

def binary_gap(n: int) -> int:
    """
    Problem 10: Binary Gap
    Given a positive integer n, find the longest distance between two consecutive 1's in the binary representation of n.
    """
    pass


# Testing each function with sample test cases
def test_function(func, args, expected):
    result = func(*args)
    if result == expected:
        print(f"{func.__name__}({args}) -> PASS")
    else:
        print(f"{func.__name__}({args}) -> FAIL (Got {result}, Expected {expected})")

if __name__ == "__main__":
    # Add test cases for each function
    test_cases = [
        (bitwise_and_of_range, (5, 7), 4),
        (single_number, ([2, 2, 3, 2],), 3),
        (count_total_set_bits, (5,), 7),  # Total set bits in numbers 1 to 5 are 1+1+2+1+2=7
        (reverse_bits, (43261596,), 964176192),  # Example: 00000010100101000001111010011100 reversed
        (maximum_xor, ([3, 10, 5, 25, 2, 8],), 28),
        (smallest_power_of_two_greater_than_or_equal, (5,), 8),
        (bit_difference, (29, 15), 2),  # 29 = 11101, 15 = 01111, need to flip 2 bits
        (hamming_weight, (11,), 3),  # 11 = 1011, has 3 set bits
        (swap_odd_even_bits, (23,), 43),  # 23 = 10111 becomes 101011 which is 43
        (binary_gap, (22,), 2)  # 22 = 10110, longest gap is 2
    ]

    # Run test cases
    for func, args, expected in test_cases:
        test_function(func, args, expected)
