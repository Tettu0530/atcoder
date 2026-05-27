N = int(input())
S = list(map(list, input().split()))

t = list("22233344455566677778889999")

c = []
for s in S:
    c.append(t[(ord(s[0]) - ord("a"))])

print("".join(c))