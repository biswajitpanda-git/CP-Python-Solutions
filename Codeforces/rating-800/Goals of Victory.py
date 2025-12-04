import sys

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index : index +n-1]))
    index += n-1

    # sum of efficiency is 0
    goals_sum = sum(arr)
    print(-1*goals_sum)