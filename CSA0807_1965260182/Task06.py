from functools import lru_cache
import sys
calls = 0
def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)
calls = 0
print("Naive:", ways_naive(25))
print("Naive calls:", calls)
calls = 0
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)
calls = 0
print("\nMemoised:", ways_memo(25))
print("Memoised calls:", calls)
print("\nValues from 1 to 6")
for n in range(1, 7):
    print(n, "=", ways_memo(n))
print("\nRecursion limit:", sys.getrecursionlimit())
try:
    print("Ways for 1000 steps:", ways_memo(1000))
except RecursionError:
    print("Recursion limit exceeded")
def ways_loop(n):
    a, b = 1, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
print("\nIterative result for 1000:")
print(ways_loop(1000))