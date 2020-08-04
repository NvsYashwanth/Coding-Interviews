
def fermatsPrime(self,n):
    a=n-2
    return pow(a,n-1)%n==1