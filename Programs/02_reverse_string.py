# Reverse a string without slicing.

def reverse_string(s):
    if s == "" or not isinstance(s, str):
        return 0
    rev=""
    length=len(s)
    for i in range(length):
         for rever in s[length-1]:
             rev=rev+rever
             length=length-1
    return rev
        
        
print(reverse_string("aayam"))
print(reverse_string(123))
