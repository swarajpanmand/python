def lent(list):
    count =0
    for i in list:
        count+=1
    return count
    
list = list(map(int, input().split()))
print(lent(list))
    
