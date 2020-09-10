def countZeros(N):
    if N==0:
        return 1
    if N<10:
        return 0
    if N%10==0:
        return 1 + countZeros(N//10)
    return countZeros(N//10)

N=int(input())
print(countZeros(N))
