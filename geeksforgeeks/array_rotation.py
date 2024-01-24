def rotate_right(arr, m ,n):
    temp = [0]*m
    temp2 = [0]*m

    for i in range(m):
        temp[i] = arr[n-i-1]
    for i in range(n-m):
        arr[n-i-1] = arr[n-i-m-1]   
    for i in range(m):
        temp2[i] = temp[m-i-1]
    for i in range(m):
        arr[i] = temp2[i]
    return arr

def left_rotate(arr, n, m):
    for i in range(m):
        rotate_left_one(arr, n)
    print(arr)

def rotate_left_one(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i]= arr[i+1]
    arr[n-1] = temp


m = int(input("enter number of time to rotate: "))
arr = list(map(int, input().split()))
n = len(arr)
# print(rotate_right(arr, m ,n))
left_rotate(arr, n, m)


