from sys import stdin
input = stdin.readline

T = int(input())
case = [list(input().rstrip()) for _ in range(T)]

out = []

for c in case:
    n = len(c)
    cnt = [0] * 26
    for s in c:
        cnt[ord(s) - ord("a")] += 1
    p = [(cnt[i], chr(ord("a") + i)) for i in range(26) if cnt[i] > 0]
    p.sort(reverse=True)
    if p[0][0] > ((n + 1) // 2):
        out.append("No")
    else:
        out.append("Yes")
        result = [None] * n
        idx = 0
        for count, ch in p:
            for _ in range(count):
                result[idx] = ch
                idx += 2
                if idx >= n:
                    idx = 1
        out.append("".join(result))

print("\n".join(out))