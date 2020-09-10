def stringToInteger(s):
    x=ord(s[0])-ord('0')
    if len(s)==1:
        return ord(s)-ord('0')
    x=x*(10**(len(s)-1))+stringToInteger(s[1:])
    return int(x)

s=input()
print(stringToInteger(s))
