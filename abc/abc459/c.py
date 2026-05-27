from sys import stdin

N, Q = map(int, stdin.readline().split())
queries = [tuple(map(int, stdin.readline().split())) for _ in range(Q)]

A = [0] * N
B = [0] * (Q + 1)

k = 0
for q in queries:
    if q[0] == 1:
        A[q[1] - 1] += 1
        B[A[q[1] - 1]] += 1
        if B[A[q[1] - 1]] == N: k += 1
    elif q[0] == 2:
        if (k + q[1]) > Q:
            print(0)
        else:
            print(B[k + q[1]])