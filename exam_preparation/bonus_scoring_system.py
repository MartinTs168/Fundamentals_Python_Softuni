from math import ceil

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
attendance_of_max_bonus_student = 0
for i in range(students):
    current_attendance = int(input())
    current_bonus = current_attendance / lectures * (5 + additional_bonus)
    if current_bonus > max_bonus:
        max_bonus = current_bonus
        attendance_of_max_bonus_student = current_attendance
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendance_of_max_bonus_student} lectures.")
