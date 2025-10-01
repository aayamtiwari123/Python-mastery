def fibbonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        while (n>2):
            c=a+b
            a=b
            b=c
            print(c)
            n=n-1

fibbonacci(10)

    
