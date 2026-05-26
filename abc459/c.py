N, Q = map(int, input().split())
q = [tuple(map(int, input().split())) for _ in range(Q)]

m = [0] * N

for query in q:
    if query[0] == 1:
        m[query[1] - 1] += 1
        if 0 not in m:
            for i in range(N):
                m[i] -= 1
    elif query[0] == 2:
        res = 0
        for i in range(N):
            if m[i] >= query[1]:
                res += 1
        print(res)