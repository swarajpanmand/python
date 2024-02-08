test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
res= [''.join(row) for row in zip(*test_list)]
res1 = [''.join(row) for row in test_list]
print(res)
print(res1)
