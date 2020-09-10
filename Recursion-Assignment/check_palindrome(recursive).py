def palindrome(s,start,end):
    if start==end:
        return 'true'
    if s[start]!=s[end]:
        return 'false'
    
    if start<end:
        smallOutput=palindrome(s,start+1,end-1)
        return smallOutput
    return 'true'

s=input()
print(palindrome(s,0,len(s)-1))   
