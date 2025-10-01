#sum of factorials

def sum_factorials(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+fact(i)
    return sum
    
def fact(n):
    if n<=996:
        if n==0:
          return 1
        else:
          return n*fact(n-1)
    else:
        factor=1
        for i in range(1,n+1):
            factor=factor*i
        return factor
     
        
print(sum_factorials(999))
