""" unit 4.1 task 2 Create functions to add(), subtract(), divide() and multiply(). All
    
    functions should read 2 values as input.      """
"""

def add(a,b):
    c = a+b
    print(c) 

def sub(a,b):
    c = a-b
    print(c) 

def mul(a,b):
    c = a*b
    print(c) 

def div(a,b):
    c = a/b
    print(c) 



first_num = int(input("enter the first number to calculate"))
second_num = int(input("enter the second number to calculate"))




add(first_num,second_num)
sub(first_num,second_num)
mul(first_num,second_num)
div(first_num,second_num)

"""


def add():
    a = float(input("enter the first number to calculate"))
    b = float(input("enter the second number to calculate"))
    result = a+b
    print(f"sum:{result}") 

def sub():
    a = float(input("enter the first number to calculate"))
    b = float(input("enter the second number to calculate"))
    result = a-b
    print(f"sum:{result}")

def mul(  ):
    a = float(input("enter the first number to calculate"))
    b = float(input("enter the second number to calculate"))
    result = a*b
    print(f"sum:{result}")

def div():
    a = float(input("enter the first number to calculate"))
    b = float(input("enter the second number to calculate"))
    if b != 0:
       result = a/b
       print(f"Quotient:{result}")
    else:
        print("Error: Division by zero is not allowed.")

add()
sub()
mul()
div()
