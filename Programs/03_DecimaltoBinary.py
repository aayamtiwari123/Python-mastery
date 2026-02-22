# Convert decimal to binary manually.

def deci_bina(dec):
    bin="0"
    reverse=""
    if dec==0:
        return bin
    while(dec!=0):
        if dec%2==0:
            bin=bin+"0"
            dec=dec//2
        else:
            bin=bin+"1"
            dec=dec//2#// is integer divison
            
    #reverse the whole thing now
    length=len(bin)-1
    for i in range(len(bin)-1):
         for rev in bin[length]:
             reverse= reverse+rev
         length=length-1
    
    return reverse

print(deci_bina(0))
print(deci_bina(1))
print(deci_bina(2))
print(deci_bina(3))
print(deci_bina(10))
print(deci_bina(45))
print(deci_bina(100))

    
            
       
