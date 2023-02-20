import sys
n= int(input())

res = []

for i in range(n):
    res.append(int(sys.stdin.readline()))

res.sort()

for i in range(n):
    print(res[i])
