n=int(input())

s=bin(n)[2:]

if s.count('1')==1:
    print("YES")
else:
    print("No")