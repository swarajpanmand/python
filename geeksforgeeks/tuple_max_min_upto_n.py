tup = (45,456,49,54,7,54)
tup = list(sorted(tup))
lent = len(tup)
res = []
for i in range(2):
    res.append(tup[i])
    res.append(tup[lent-i-1])
print(res)