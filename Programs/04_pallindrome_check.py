def pallindrome_check(s):
    mem=s
    emp=""
    length=len(s)-1
    for i in range(length+1):
        for rev in s[length]:
            emp=emp+rev
        length=length-1
    
    if emp==mem:
        return True
    else:
        return False

print(pallindrome_check("dad"))
        
