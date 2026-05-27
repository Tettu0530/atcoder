import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
A = input().strip().split()

r = A[-K:] + A[:-K]
print(" ".join(r))