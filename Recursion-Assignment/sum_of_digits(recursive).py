def sum(N):
    a=len(N)
    if a==0:
        return 0
    smallOutput=sum(N[1:])
    return int(N[0])+smallOutput

N=input()
print(sum(N))
