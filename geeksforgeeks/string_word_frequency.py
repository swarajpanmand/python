s= "forforfor"
k= "for"
count=0
for i in range(len(s)-len(k)+1):
    if s[i:i+len(k)] == k:
        count+=1
print(count)