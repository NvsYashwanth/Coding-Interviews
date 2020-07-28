#code

tests=int(input())
for i in range(tests):
    n=int(input())
    state=1
    m=int(n**0.5)+1
    for i in range(2,m+1):
        if n%i==0:
            state=0
            break
    if state==1:
        print("Yes")
    else:
        print("No")