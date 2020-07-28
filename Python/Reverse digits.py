n=int(input())

# Approach 1 - o(n)
# Just convert to string and reverse

# Approach 2 - o(n)
z=0
remaining=abs(n)
while(remaining):
    z*=10
    z+=(remaining%10)
    remaining//=10
z=(z-2*z if n<0 else z)
    