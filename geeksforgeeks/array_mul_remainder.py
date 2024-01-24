def mul(arr , n):
    mul=1
    for i in range(n):
        mul = mul*arr[i]
    return mul

def remainder(arr, n ):
    rem=0
    p = mul(arr, n)
    rem =p%n
    return rem

arr = list(map(int, input().split()))
n = len(arr)
print(remainder(arr, n))