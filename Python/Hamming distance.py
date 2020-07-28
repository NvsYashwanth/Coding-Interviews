x=int(input())
y=int(input())
z=x^y
c=0
while(z):
    c+=z&1
    z>>=1
print(c)