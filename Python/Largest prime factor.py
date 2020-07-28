
tests=int(input())
for i in range(tests):
    n=int(input())
    while(n%2==0):
        prime=2
        n>>=1

    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            prime=i
            n//=i

    if n>2:
        prime=n

    print(prime)