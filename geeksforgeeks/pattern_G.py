n=int(input())
print(" ", end="")
print("*"*(n-4))
for i in range(n-2):
    if(i == (n//2-1)):
        print("*",end="")
        print(" "*(n-6), end="")
        print("*"*3)
    else:
        if(i>(n//2-1)):
            print("*",end="")
            print(" "*(n-4),end="")
            print("*")
        else:
            print("*")
print(" ",end="")
print("*"*(n-4))