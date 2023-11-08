courses = {}
command = input()
while command != 'end':
    course_name = command.split(' : ')[0]
    student_name = command.split(' : ')[1]
    if course_name in courses.keys():
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]
    command = input()
for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")