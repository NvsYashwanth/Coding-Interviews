n=int(input())

s=bin(n)[2:]

if s.count('1')==1 and s.count('0')%2==0:
    print("YES")
else:
    print("No")