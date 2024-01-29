def exists(list, m):
    # for c in list:
    #     if (m==c):
    #         return True
    # return False
    if m in list:
        return True
    return False


list = list(map(int, input().split()))
m = int(input())
n = len(list)
print(exists(list, m))