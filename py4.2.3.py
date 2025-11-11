#Create recursive function to find sum of digits


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        last_digit = n % 10
        remaining = n // 10
        return last_digit + sum_of_digits(remaining)
                  # 4+3+2+1(0)

# Example
print("Sum of digits:", sum_of_digits(1234))  # Output: 10







def sum_of_digits(n):
    if n==0:
        return 0
    else:
        get_last_num =  n % 10
        throught_out_last_num = n // 10

    return get_last_num + sum_of_digits(throught_out_last_num)
                              # 4+3+2+1(0)

num = int(input("enter the number you sum :  "))    

sum = sum_of_digits(num)
print( f"sum_of_digits:{sum}")



"""
print(1234 % 10)
print(1234 / 10)
print(1234 // 10)
print(123 % 10)
print(123 // 10)
print(12 % 10)
print(12 // 10)
print(1 % 10)
print(1 // 10)



print(125654844 % 10)
print(125654844 / 10)
"""