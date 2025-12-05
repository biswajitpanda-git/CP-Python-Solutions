import sys

data = sys.stdin.read().split()
iterator = iter(data)

if data:
    t = int(next(iterator))

    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))
        x = int(next(iterator))

        min_sum = k * (k + 1) // 2
        max_sum = k * (2 * n - k + 1) // 2
        
        # check if x falls within the range
        if min_sum <= x <= max_sum:
            print("YES")
        else:
            print("NO")

# TC: O(1) per test case. The math formulas are constant time.
# SC: O(1)