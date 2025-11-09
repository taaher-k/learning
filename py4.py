
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

second_max = 0
for num in input_list:
    if num != maximun:
        second_max < num
        second_max = num

print(f" second maximum number is {second_max}")