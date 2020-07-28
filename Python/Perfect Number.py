# Euclids Algorithm
tests=int(input())

for i in range(tests):
    n=int(input())

    p=2
    res=0
    while(res<n):
        res=(2**(p-1))*((2**p)-1)
        p+=1
    if res==n:
        print(1)
    else:
        print(0)