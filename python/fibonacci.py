# brute force
# space - O(n) -> each recursive call creates a new stack frame
# time - O(2^n)
def fib_brute(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return fib_brute(n - 1) + fib_brute(n - 2)

# using array
# space - O(n)
# time - O(n)
def fib_arr(n):
    if n == 1:
        return 0
    
    arr = [0] * n
    arr[1] = 1

    for i in range(2, n):
        arr[i] = arr[i - 2] + arr[i - 1]

    return arr[n - 1]


# fully optimized in space/time
# space - O(1)
# time - O(n)
def fib(n):
    if n == 1:
        return 0
    
    if n == 2:
        return 1

    num1 = 0
    num2 = 1

    for _ in range(n - 2):
        num1, num2 = num2, num1 + num2

    return num2
