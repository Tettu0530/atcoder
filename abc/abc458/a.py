import sys
input = sys.stdin.readline

S = list(input())
N = int(input())
r = S[N:]
r = r[:-(N+1)]

print("".join(r))