def swap(list):
    list[0], list[-1] = list[-1], list[0]
    return list

list = list(map(int, input().split()))
print(swap(list))