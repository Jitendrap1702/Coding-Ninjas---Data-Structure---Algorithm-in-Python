def checkAB(string):
    smallAnswer= False

    if len(string)==0:
        return True

    if len(string)==1:
        if string[0]=='a':
            smallAnswer=True
    
    elif len(string)==2:
        if string[0]=='a' and string[1]=='a':
            smallAnswer=True
    
    elif len(string)>=3:
        if string[0]=='a' and string[1]=='a':
            smallAnswer=True
            smallOutput=checkAB(string[1:])
            return smallOutput

        elif string[0]=='a' and string[1:3]=='bb':
            smallAnswer=True
            smallOutput=checkAB(string[3:])
            return smallOutput

    return smallAnswer

string=input()
result=checkAB(string)

if result is True:
