import sys
from collections import Counter

data = sys.stdin.read().split()
iterator = iter(data)

if data:
    t = int(next(iterator))

    for _ in range(t):
        n = int(next(iterator))
        k = int(next(iterator))

        s = next(iterator)

        freq = Counter(s)
        odd_counts = 0
        for count in freq.values():
            if count%2 != 0:
                odd_counts += 1
        if odd_counts <= k+1:
            print("YES")
        else:
            print("NO")
