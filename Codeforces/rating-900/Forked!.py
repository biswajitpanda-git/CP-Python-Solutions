import sys

data = sys.stdin.read().split()
iterator = iter(data)
t = int(next(iterator))

dx = [-1, 1, -1, 1]
dy = [-1, -1, 1, 1]

for _ in range(t):
    a = int(next(iterator))
    b = int(next(iterator))
    xk = int(next(iterator))
    yk = int(next(iterator))
    xq = int(next(iterator))
    yq = int(next(iterator))

    king_hits = set()
    queen_hits = set()

    for j in range(4):
        king_hits.add((xk + dx[j]*a, yk + dy[j]*b))
        queen_hits.add((xq + dx[j]*a, yq + dy[j]*b))

        king_hits.add((xk + dx[j]*b, yk + dy[j]*a))
        queen_hits.add((xq + dx[j]*b, yq + dy[j]*a))

        ans = 0
        for pos in king_hits:
            if pos in queen_hits:
                ans += 1
    print(ans)

                       


