def monotonic(arr, n):
    return(
        all(arr[i]<=arr[i+1] for i in range(n-1)) or
        all(arr[i]>=arr[i+1] for i in range(n-1))
    )

arr = list(map(int, input().split()))
n = len(arr)
print(monotonic(arr, n))