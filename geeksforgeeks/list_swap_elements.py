def swap(list, n, m):
    list[n], list[m] = list[m], list[n]
    return list

list = list(map(int, input().split()))
n , m = map (int, input().split())
print(swap(list, n,m))