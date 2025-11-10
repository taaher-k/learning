"""

#1

def student_report():
    name = input("enter the student name : ")
    marks_input = input("enter the marks separated by space:  ")

    marks = []
    for x in marks_input.split():
        marks.append(int(x))

    total = 0
    for y in marks:
        total += y

    average = total / len(marks)


    return name, total, average

student_name,student_total_marks,student_average_marks = student_report()

print(f"student_name: {student_name}")
print(f"student_total_marks: {student_total_marks}")
print(f"student_average_marks: {student_average_marks}")



#2

def student_marks_manager():
    student_name = input("enter the student name : ")
    marks = [map(int, input("enter the marks separated by space: ").split()) ]

    print(f"{student_name} {marks}")

student_marks_manager()



"""
#3

def student_marks_manager():
    student_name = input("Enter the student name: ")
    marks = list(map(int, input("Enter the marks separated by space: ").split()))

    print(f"Student Name: {student_name}")
    print(f"Marks: {marks}")
    print(f"Total: {sum(marks)}")
    print(f"Average: {sum(marks)/len(marks):.2f}")

student_marks_manager()
