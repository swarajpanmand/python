# def navigate(arr,M,N):
#     arr2 = []
#     while len(arr2)!= M*N:
#         for k in range(100):
#             i = k
#             for j in range(k,N):
#                 arr2.append(arr[i][j])
#                 print(arr2)
#             if len(arr2)== M*N:
#                 break 
            
#             j = N-1
#             i=k
#             for i in range(k,M):
#                 arr2.append(arr[i][j])
#                 print(arr2)
#             if len(arr2)== M*N:
#                 break 

#             i = M-1
#             j=k
#             for j in range(N-1, k, -1):
#                 arr2.append(arr[i][j])
#                 print(arr2)
#             if len(arr2)== M*N:
#                 break 
    
#             j=k
#             i=k
#             for j in range(M-1, 1+k, -1):
#                 arr2.append(arr[i][j])
#                 print(arr2)
#             if len(arr2)== M*N:
#                 break 
        
#         M=M-2
#         N = N-2

# n = int(input())
# M, N = map(int, input().split())
# arr = [[0 for _ in range(N)] for _ in range(M)]
# for i in range(M):
#     # arr = list(map (int, input().split))
#     for j in range(N):
#         arr[i][j] = int(input())
#     print()
# print(arr)
# navigate(arr,M,N)

def navigate(arr, M, N):
    arr2 = []
    while len(arr2) != M * N:
        for k in range(100):
            i = k
            for j in range(k, N):
                arr2.append(arr[i][j])
            if len(arr2) == M * N:
                break

            j = N - 1
            i = k
            for i in range(k + 1, M):
                arr2.append(arr[i][j])
            if len(arr2) == M * N:
                break

            i = M - 1
            j = N - 2 - k
            for j in range(N - 2 - k, k - 1, -1):
                arr2.append(arr[i][j])
            if len(arr2) == M * N:
                break

            j = k
            i = M - 2 - k
            for i in range(M - 2 - k, k, -1):
                arr2.append(arr[i][j])
            if len(arr2) == M * N:
                break

        M -= 2
        N -= 2
    return arr2

n = int(input())
M, N = map(int, input().split())
arr =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# arr = [[0 for _ in range(N)] for _ in range(M)]
# for i in range(M):
#     arr[i] = list(map(int, input().split()))

print(navigate(arr, M, N))
