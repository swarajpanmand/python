dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

def merge(dict1, dict2):
    return dict2.update(dict1)

print(merge(dict1, dict2)) #prints None nothing

print(dict1)
merge(dict2, dict1)
print(dict1)
merge(dict1, dict2)
print(dict2)