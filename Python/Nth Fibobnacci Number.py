
# Approach 1

n=int(input())

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
        
    return fib(n-1)+fib(n-2)

#---------------------------------------------------------

# Approach 2
# Function for nth fibonacci number - Space Optimisataion 
# Taking 1st two fibonacci numbers as 0 and 1 
  
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n+1): 
            c = a + b 
            a,b = b,c 
        return b 
print(fibonacci(9)) 
  
