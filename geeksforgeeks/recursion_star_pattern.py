def star(n):
    print("*"*n)
   
def ulta(n1,n):
    
    star(n1)
    n1 =n1+ 1
    if n1 == n+1:
        return
    ulta(n1,n)

ulta(1,5)