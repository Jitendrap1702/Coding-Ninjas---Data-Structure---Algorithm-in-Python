if input = 4
output will be 1.93750  so we use %0.5f here

def geometricSum(k):
    if k==0:
        return 1
    smallOutput=geometricSum(k-1)
    return ((1/2)**k) + smallOutput

k=int(input())
print('%.5f'%geometricSum(k))
