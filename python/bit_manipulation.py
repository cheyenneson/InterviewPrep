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
    for i in range(len(nums)):
        triplet = False
        for j in range(i + 1, len(nums)):
            if nums[i] ^ nums[j] == 0:
                triplet = True
                break
        else:
            if not triplet:
                return nums[i]
                


def count_total_set_bits(n: int) -> int:
    """
    Problem 3: Count Total Set Bits
    Given a positive integer n, count the total number of set bits (1s) in binary representation of all numbers from 1 to n.
    """
    result = 0
    for i in range(1, n + 1):
        hamm_weight = 0
        val = i
        while val:
            val &= val - 1
            hamm_weight += 1
        result += hamm_weight
    return result

def reverse_bits(x: int) -> int:
    """
    Problem 4: Reverse Bits
    Given a 32-bit unsigned integer, reverse its bits and return the resulting integer.
    """
    result = 0
    for _ in range(32):
        result <<= 1
        result += x & 1
        x >>= 1
    return result

def maximum_xor(nums: list[int]) -> int:
    """
    Problem 5: Maximum XOR of Two Numbers in an Array
    Given a non-empty array of numbers, find the maximum result of a pair of numbers' XOR in that array.
    """
    max = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] ^ nums[j] > max:
                max = nums[i] ^ nums[j]
    return max

def smallest_power_of_two_greater_than_or_equal(x: int) -> int:
    """
    Problem 6: Smallest Power of Two Greater than or Equal to n
    Given an integer x, find the smallest power of 2 greater than or equal to x.
    """
    if x == 0:
        return 1
    elif x & (x - 1) == 0:
        return x
    else:
        pos = -1
        while x:
            x >>= 1
            pos += 1
        return 1 << pos + 1



def bit_difference(a: int, b: int) -> int:
    """
    Problem 7: Bit Difference
    Given two integers a and b, return the number of bits that need to be flipped to convert a to b.
    """
    val = a ^ b
    hamm_weight = 0
    while val:
        val &= (val - 1)
        hamm_weight += 1
    return hamm_weight

def hamming_weight(n: int) -> int:
    """
    Problem 8: Hamming Weight
    Given an unsigned integer n, return the number of '1' bits it has (also known as the population count).
    """
    hamm_weight = 0
    while n:
        n &= (n - 1)
        hamm_weight += 1
    return hamm_weight

def swap_odd_even_bits(n: int) -> int:
    """
    Problem 9: Swap Odd and Even Bits
    Given an unsigned integer n, swap all odd bits with even bits. (For example, bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on.)
    """
    count = 0
    result = 0
    while n:
        rightmost = n & 3
        swapped = ((rightmost & 1) << 1) + ((rightmost & 2) >> 1)
        n >>= 2
        result += swapped << (count * 2)
        count += 1
    return result


def binary_gap(n: int) -> int:
    """
    Problem 10: Binary Gap
    Given a positive integer n, find the longest distance between two consecutive 1's in the binary representation of n.
    """
    left = -1
    right = 0
    val = n

    while val & 1 != 1:
        val >>= 1
        right += 1
    
    val = n
    while val:
        val >>= 1
        left += 1

    return left - right - 1


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



# need to review grade:
# Thank you for sharing your solutions! Let's go through each function one by one to identify any potential optimizations and correctness issues.

# ### 1. **`bitwise_and_of_range(m, n)`**

# **Your Solution**:
# ```python
# result = m
# for i in range(m + 1, n + 1):
#     result &= i
# return result
# ```

# **Feedback**:
# - This solution is correct but inefficient, especially when `n - m` is large. The time complexity is \(O(n-m)\), which can be optimized.
# - A more efficient approach is to use the bit-shift technique to find the common prefix of `m` and `n`:

# **Optimized Solution**:
# ```python
# def bitwise_and_of_range(m: int, n: int) -> int:
#     while m < n:
#         n &= (n - 1)
#     return n
# ```
# - This has a time complexity of \(O(\log n)\), which is much faster.

# ---

# ### 2. **`single_number(nums)`**

# **Your Solution**:
# ```python
# for i in range(len(nums)):
#     triplet = False
#     for j in range(i + 1, len(nums)):
#         if nums[i] ^ nums[j] == 0:
#             triplet = True
#             break
#     else:
#         if not triplet:
#             return nums[i]
# ```

# **Feedback**:
# - The current solution has a time complexity of \(O(n^2)\), which is not efficient for large lists.
# - This problem can be solved using bitwise manipulation with a linear scan using bit-counting. The idea is to use a bit mask to track counts of bits across all numbers.

# **Optimized Solution**:
# ```python
# def single_number(nums: list[int]) -> int:
#     ones, twos = 0, 0
#     for num in nums:
#         ones = (ones ^ num) & ~twos
#         twos = (twos ^ num) & ~ones
#     return ones
# ```
# - The above solution has a time complexity of \(O(n)\) and uses constant space.

# ---

# ### 3. **`count_total_set_bits(n)`**

# **Your Solution**:
# ```python
# result = 0
# for i in range(1, n + 1):
#     hamm_weight = 0
#     val = i
#     while val:
#         val &= val - 1
#         hamm_weight += 1
#     result += hamm_weight
# return result
# ```

# **Feedback**:
# - Your solution is correct but can be optimized. The time complexity is \(O(n \log n)\).
# - A more efficient approach involves using patterns in binary counts, reducing it to \(O(\log n)\):

# **Optimized Solution**:
# ```python
# def count_total_set_bits(n: int) -> int:
#     count = 0
#     i = 1
#     while i <= n:
#         total_pairs = (n + 1) // (i * 2)
#         count += total_pairs * i
#         remainder = (n + 1) % (i * 2)
#         count += max(0, remainder - i)
#         i <<= 1
#     return count
# ```

# ---

# ### 4. **`reverse_bits(x)`**

# **Your Solution**:
# ```python
# result = 0
# for _ in range(32):
#     result <<= 1
#     result += x & 1
#     x >>= 1
# return result
# ```

# **Feedback**:
# - The solution is correct, but you can optimize it by using Python's built-in bit manipulation.

# **Optimized Solution**:
# ```python
# def reverse_bits(x: int) -> int:
#     return int(bin(x)[2:].zfill(32)[::-1], 2)
# ```

# ---

# ### 5. **`maximum_xor(nums)`**

# **Your Solution**:
# ```python
# max = 0
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] ^ nums[j] > max:
#             max = nums[i] ^ nums[j]
# return max
# ```

# **Feedback**:
# - The current solution has a time complexity of \(O(n^2)\).
# - This can be optimized using a bitwise Trie, reducing the time complexity to \(O(n)\).

# **Optimized Solution**:
# ```python
# def maximum_xor(nums: list[int]) -> int:
#     max_xor = 0
#     mask = 0
#     for i in range(31, -1, -1):
#         mask |= (1 << i)
#         prefixes = {num & mask for num in nums}
#         tmp = max_xor | (1 << i)
#         if any(tmp ^ prefix in prefixes for prefix in prefixes):
#             max_xor = tmp
#     return max_xor
# ```

# ---

# ### 6. **`smallest_power_of_two_greater_than_or_equal(x)`**

# **Your Solution**:
# ```python
# if x == 0:
#     return 1
# elif x & (x - 1) == 0:
#     return x
# else:
#     pos = -1
#     while x:
#         x >>= 1
#         pos += 1
#     return 1 << pos + 1
# ```

# **Feedback**:
# - This can be simplified using a one-liner.

# **Optimized Solution**:
# ```python
# def smallest_power_of_two_greater_than_or_equal(x: int) -> int:
#     return 1 if x == 0 else 1 << (x - 1).bit_length()
# ```

# ---

# ### 7. **`bit_difference(a, b)`**

# Your solution is optimal:
# ```python
# val = a ^ b
# hamm_weight = 0
# while val:
#     val &= (val - 1)
#     hamm_weight += 1
# return hamm_weight
# ```

# ### 8. **`hamming_weight(n)`**

# Your solution is also optimal:
# ```python
# hamm_weight = 0
# while n:
#     n &= (n - 1)
#     hamm_weight += 1
# return hamm_weight
# ```

# ### 9. **`swap_odd_even_bits(n)`**

# **Your Solution**:
# ```python
# count = 0
# result = 0
# while n:
#     rightmost = n & 3
#     swapped = ((rightmost & 1) << 1) + ((rightmost & 2) >> 1)
#     n >>= 2
#     result += swapped << (count * 2)
#     count += 1
# return result
# ```

# **Feedback**:
# - Your solution is correct but can be simplified using masks.

# **Optimized Solution**:
# ```python
# def swap_odd_even_bits(n: int) -> int:
#     return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
# ```

# ---

# ### 10. **`binary_gap(n)`**

# **Your Solution**:
# ```python
# left = -1
# right = 0
# val = n

# while val & 1 != 1:
#     val >>= 1
#     right += 1

# val = n
# while val:
#     val >>= 1
#     left += 1

# return left - right - 1
# ```

# **Feedback**:
# - Your solution doesn't account for multiple gaps. This can be optimized:

# **Optimized Solution**:
# ```python
# def binary_gap(n: int) -> int:
#     prev = None
#     max_gap = 0
#     for i in range(n.bit_length()):
#         if (n >> i) & 1:
#             if prev is not None:
#                 max_gap = max(max_gap, i - prev)
#             prev = i
#     return max_gap
# ```

# ---

# ### Summary of Optimizations
# - Several functions had inefficient solutions, particularly `bitwise_and_of_range`, `single_number`, and `maximum_xor`. Optimizing these can greatly improve performance, especially for large inputs.
# - Some solutions could be simplified using Python’s built-in functions or bit manipulation tricks.

# Feel free to test the optimized solutions and let me know if you encounter any issues!