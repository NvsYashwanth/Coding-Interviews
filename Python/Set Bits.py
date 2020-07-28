n=int(input())
z=[0,1]+[0]*(n-1)
c=1
for i in range(2,n+1):
    z[i]=z[i>>1]+(i&1)
    c+=z[i]