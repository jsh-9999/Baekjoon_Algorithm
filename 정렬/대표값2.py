res = []
for i in range(5):
    res.append(int(input()))

res.sort()
sum = sum(res)
avg = sum/5
print(round(avg))

print(res[2])
