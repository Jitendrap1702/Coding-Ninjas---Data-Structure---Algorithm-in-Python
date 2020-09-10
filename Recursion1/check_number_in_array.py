def checkNumber(arr, x):
    if len(arr)==0:
        return False
    if arr[0]==x:
        return True
    #we can only return here
    #return checkNumber(arr[1:],x)
    #or we can write this line 9 to 13    
    smallerArray=arr[1:]
    checkSmallerArray=checkNumber(smallerArray,x)
    if checkSmallerArray:
        return True
    return False


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
if checkNumber(arr, x):
    print('true')
else:
    print('false')
