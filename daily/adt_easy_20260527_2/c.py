N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def r(g: list[list[int]]):
    return [
        list(row) for row in zip(*g[::-1])
    ]

all = [A]
g = A
for _ in range(3):
    g = r(g)
    all.append(g)

for x in all:
    ok = True
    for i in range(N):
        for j in range(N):
            if x[i][j] == 1 and B[i][j] != 1:
                ok = False
                break
        if not ok:
            break
    if ok:
        print("Yes")
        exit(0)
print("No")