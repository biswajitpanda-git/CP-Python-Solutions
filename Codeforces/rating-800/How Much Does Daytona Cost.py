import sys

input = sys.stdin.read
data = input().split()
index =0

t = int(data[index])
index += 1
for _ in range(t):
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    arr = list(map(int, data[index:index + n]))
    index += n
    if k in arr:
        print("YES")
    else:
        print("NO")