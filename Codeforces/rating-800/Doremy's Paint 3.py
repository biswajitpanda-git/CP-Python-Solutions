import sys
from collections import Counter

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index +n]))
    index += n
    frequency_map = Counter(a)
    if len(frequency_map)>=3:
        print("No")
    else:
        freq_iterator = iter(frequency_map.values())
        freq_1 = next(freq_iterator)
        freq_2 = next(freq_iterator) if len(frequency_map) == 2 else freq_1

        if freq_1 == freq_2:
            print("Yes")
        elif n%2 ==1 and abs(freq_1 - freq_2) == 1:
            print("Yes")
        else:
            print("No")