def max(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max


arr = list(map(int, input().split()))
print(max(arr))
