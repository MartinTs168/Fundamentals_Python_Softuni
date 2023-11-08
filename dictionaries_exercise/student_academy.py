students = {}
num_lines = int(input())
for _ in range(num_lines):
    name = input()
    grade = float(input())
    if name not in students.keys():
        students[name] = [grade]
    else:
        students[name].append(grade)
for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
