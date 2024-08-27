# Enter your code here. Read input from STDIN. Print output to STDOUT
students_of_english_newspaper = int(input())
student_roll_number_english_newspaper = set(list(map(int, input().split())))
students_of_french_newspaper = int(input())
student_roll_number_french_newspaper = set(list(map(int, input().split())))

total_students = len(student_roll_number_english_newspaper.difference(student_roll_number_french_newspaper))

print(total_students)