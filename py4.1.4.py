"""   Write function to read a number as input and return digits as list.   """
""" con_to_digit = list(map(int, read_num.split())) """





def get_digits():
    num = input("enter the digits that you want to convert :  ")

    digits = [int(dit) for dit in num]

    return digits

digits_r = get_digits()
print(f"digits = {digits_r}")








def num_to_list():
    read_num = input("enter the number greater then 100 ")
    con_to_digit = list(int(ch) for ch in read_num if '0' <= ch <= '9')
    print (con_to_digit)
num_to_list() 




"""def num_to_list():
    read_num = input("Enter a number greater than 100: ")
    con_to_digit = [int(ch) for ch in read_num if '0' <= ch <= '9']
    print("Digits as list:", con_to_digit)

num_to_list()
"""


"""def get_digits():
    number = input("Enter a number: ")
    digits = [int(d) for d in number if d.isdigit()]
    return digits
"""

"""
def get_digits():
    number = input("Enter a number: ")
    digits = list(map(int, filter(str.isdigit, number)))
    return digits

"""

"""
def get_digits():
    number = input("Enter a number: ")
    i = 0
    digits = []
    while i < len(number):
        ch = number[i]
        if '0' <= ch <= '9':
            digits += [int(ch)]
        i += 1
    return digits

"""