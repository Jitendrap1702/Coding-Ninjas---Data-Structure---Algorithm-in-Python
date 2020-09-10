def sumArray(arr):
    if len(arr)==1:
        return arr[0]
    smallerArray=arr[1:]
    sumSmallerArray=sumArray(smallerArray)
    sum = arr[0]+sumSmallerArray
    return sum
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
