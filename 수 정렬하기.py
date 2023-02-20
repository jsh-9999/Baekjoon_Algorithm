h = int(input())
res = []
for i in range(h):
    res.append(int(input()))

res.sort()

for i in range(len(res)):
    print(res[i])