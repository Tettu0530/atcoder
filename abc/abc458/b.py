import sys
input = sys.stdin.readline

H, W = map(int, input().split())

r = [[0] * W for _ in range(H)]

dij = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(H):
    for j in range(W):
        for di, dj in dij:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W:
                r[i][j] += 1

for i in r:
    print(*i)