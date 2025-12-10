import sys 

data = sys.stdin.read().split()
index = 0

if data:
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1

        a = list(map(int, data[index : index + n]))
        index += n

        hashSet = set(a)
        while 1:
            c = len(hashSet)
            if c in hashSet:
                print(c)
                break
            else:
                hashSet.add(c)

