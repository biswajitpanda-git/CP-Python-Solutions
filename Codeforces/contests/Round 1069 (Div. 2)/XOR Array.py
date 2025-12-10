import sys 

data = sys.stdin.read().split()
iterator = iter(data)

if data:
    t = int(next(iterator))
    results = []

    for _ in range(t):
        n = int(next(iterator))
        l = int(next(iterator))
        r = int(next(iterator))

        p = list(range(n+1))
        p[r] = p[l-1]
        ans = []
        for i in range(n):
            val = p[i+1] ^ p[i]
            ans.append(str(val))

        results.append(" ".join(ans))
    sys.stdout.write("\n".join(results))