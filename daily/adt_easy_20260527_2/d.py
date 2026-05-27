N = int(input())

res = [[0] * N for _ in range(N)]

r, c = 0, (N - 1) // 2
res[r][c] = 1

for i in range(2, N * N + 1):
    nr, nc = (r - 1) % N, (c + 1) % N
    if res[nr][nc] == 0:
        r, c = nr, nc
    else:
        r, c = (r + 1) % N, c
    res[r][c] = i

for i in res:
    print(*i)