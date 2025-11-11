#Create recursive function to find factorial of a number.

"""



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = 4
print(f"Factorial of {num} is {factorial(num)}")




"""
"""
#2

def factorial(n):
    print(f"Calling factorial({n})")
    if n == 0 or n == 1:
        print(f"Reached base case: factorial({n}) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"Returning: {n} * factorial({n-1}) = {result}")
        return result

# Try it out
factorial(7)
"""
"""

def fibonacci(n):
    print(f"Calling fibonacci({n})")
    if n == 0:
        print("Base case: fibonacci(0) = 0")
        return 0
    elif n == 1:
        print("Base case: fibonacci(1) = 1")
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        print(f"Returning: fibonacci({n}) = {result}")
        return result

# Try it out
fibonacci(5)






"""

#1

f = 1

def fact(n):
    global f
    if (n>=1):
        f = f*n
        fact(n-1)
        
    return f    
result = fact(3)

print("factorial = ",result)



#2


def facts(x):
    if (x==1): #if(x>=1) not working ?
      return 1
    return  x * facts(x-1)       
resultl = facts(3)
print("factorial = ",resultl)



#3

def facts(x):
    if x == 0 or x == 1:
        return 1
    return x * facts(x - 1)

resultl = facts(3)
print("factorial =", resultl)


