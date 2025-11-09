
""""

def find_maximum(numbers):
    Returns the maximum number from the list.
    return max(numbers)




def find_second_maximum(numbers):
    Returns the second maximum number from the list.
    max_num = find_maximum(numbers)
    # Remove all occurrences of the maximum number
    numbers_without_max = [num for num in numbers if num != max_num]
    if numbers_without_max:
        return max(numbers_without_max)
    else:
        return None  # No second max if all elements are the same


# Example usage
input_list = list(map(int, input("Enter numbers separated by space: ").split()))
max_num = find_maximum(input_list)
second_max = find_second_maximum(input_list)

print("Maximum number:", max_num)
if second_max is not None:
    print("Second maximum number:", second_max)
else:
    print("No second maximum found (all elements may be equal).")

    
    """
"""
def find_maximum(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num>max_num:
            max_num = num
    return max_num


input_string = input("enter numbers by separated by space: ")
input_list = []
for value in input_string.split():
    input_list.append(int(value))




maximun = find_maximum(input_list)

print("Maximum number is :",maximun)

second_max = None
for num in input_list:
    if num != maximun:
       if second_max is None or num > second_max:
            second_max = num

if second_max is not None:
    print(f"Second maximum number is: {second_max}")
else:
    print("No second maximum found (all elements may be equal).")


"""



"""


def smaximumnum(number):
    msxnum = number[0]
    for num in number:
        if num>msxnum:
            msxnum = num
    return msxnum        



input_s = input("enter the numbers separated by space ")
input_l = []

for val in input_s.split():
    input_l.append(int(val))




vvdvd = smaximumnum(input_l)

print("Maximum number is :",vvdvd)


secmax  = None
for num in input_l:
    if num != vvdvd:
        if secmax is None or num > secmax:
            secmax = num

if secmax is not None:
    print(f"the second largest number is : {secmax}")
else:
    print("No second maximum found (all elements may be equal).")







"""

"""
def find_maximum(x):
    y = x[0]
    for i in x :
        if i > y:
            y=i
    return y
        

input_String = input("enter the numbers separated by space : ")
input_list = []

for num in input_String.split():
     input_list.append(int(num))

     number = input_list
maximum = find_maximum(number)

print(f"the first maximum number is : {maximum}")



sec = None
 
for num in number:
       if maximum != num:
         if sec is None or num > sec:
             sec = num
 



if sec is not None:
   print(f"the second maximum number is : {sec}")
else:
   print(f"there is no second maximum or every other number is equal")   




---

### ✅ Final Corrected Version

```python
def find_maximum(x):
  y = x[0]
  for i in x:
      if i > y:
          y = i
  return y

input_String = input("Enter the numbers separated by space: ")
input_list = []

for num in input_String.split():
  input_list.append(int(num))  # ✅ Fixed

number = input_list
maximum = find_maximum(number)
print(f"The first maximum number is: {maximum}")

def second_max():
  sec = None
  for num in number:
      if num != maximum:  # ✅ Fixed
          if sec is None or num > sec:
              sec = num
  return sec

second = second_max()
if second is not None:
  print(f"The second maximum number is: {second}")
else:
  print("There is no second maximum or every other number is equal.")
"""



def find_first_maximum_number(x):
    return max(x)

num_list = list(map(int, input("enter the numbers separated by space : ").split()))

first_max = find_first_maximum_number(num_list)

print(first_max)


def sec_max_num(x):
    first_max = find_first_maximum_number(x)

    not_first_max = [num for num in x if num != first_max]
    if not_first_max:
        return max(not_first_max)
    else:
        return None
    
sec_max =  sec_max_num(num_list)
if sec_max is not None:
  print(f"The second maximum number is: {sec_max}")
else:
  print("There is no second maximum or every other number is equal.")










"""
second_max = None

for num in num_list:
    if num != first_max:
        if second_max is None or num > second_max:
            second_max = num

if second_max is not None:
    print(second_max)
else:
    print("eq")    """