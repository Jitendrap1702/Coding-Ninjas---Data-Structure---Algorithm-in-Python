def power_num(x,n):
    if n==0:
        return 1
    smalloutput=power_num(x,n-1)
    return x*smalloutput

p=list(map(int,input().split()))
x=p[0]
n=p[1]
print(power_num(x,n))
