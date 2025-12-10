import sys

data = sys.stdin.read().split()
index = 0

s = data[0]
number = s[8:]
n = len(number)
arr = list(map(int, number[:n-1]))
print(arr)
