import sys 

data = sys.stdin.read().split()
index = 0

t = int(data[index])
index += 1

for _ in range(t):
    n = int(data[index])
    index += 1
    b = list(map(int, data[index : index+n]))
    index += n
    a =list()
    a.append(b[0])
    for i in range(1, n):
        if b[i] >= b[i-1]:
            a.append(b[i])
        else:
            a.append(b[i])
            a.append(b[i])
    print(len(a))
    print(*a)