import sys

N = int(sys.stdin.readline())
A = []
for i in range(N):
    a = int(sys.stdin.readline())
    A.append(a)
A.sort()
for j in A:
    print(j)
