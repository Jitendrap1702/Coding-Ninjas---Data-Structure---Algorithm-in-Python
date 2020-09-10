def merge(a1,a2,arr):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            arr[k]=a1[i]
            i=i+1
            k=k+1
        else:
            arr[k]=a2[j]
            j=j+1
            k=k+1

    while i<len(a1):
        arr[k]=a1[i]
        k=k+1
        i=i+1

    while j<len(a2):
        arr[k]=a2[j]
        k=k+1
        j=j+1

def mergeSort(arr, start, end):
    # Please add your code here
    if len(arr)==0 or len(arr)==1:
        return 
    mid=(start+end)//2
    a1=arr[0:mid]
    a2=arr[mid:]

    mergeSort(a1,0,mid)
    mergeSort(a2,mid,len(arr)-1)

    merge(a1,a2,arr)
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)
