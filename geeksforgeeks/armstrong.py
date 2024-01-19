n = int(input())
s = n
b =len(str(n))
sum =0

while n>0:
    r = n%10
    sum = sum + pow(r,b)
    n = n//10

if sum == s:
    print("Armstrong")
else:
    print("Not Armstrong")
