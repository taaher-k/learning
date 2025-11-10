""" unit 4.1 task 2 Create functions to add(), subtract(), divide() and multiply(). All
    
    functions should read 2 values as input.      """


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

