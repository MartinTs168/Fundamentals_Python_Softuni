students = {}
course_to_print = ''
while True:
    command = input()
    if command.islower():
        course_to_print = command.replace('_', ' ')
        break
    information = command.split(':')
    name = information[0]
    student_id = int(information[1])
    course = information[2]
    students[student_id] = {'name': name, 'course': course}

for student_id, student_info in students.items():
    if student_info['course'] == course_to_print:
        print(f"{student_info['name']} - {student_id}")

