black_list = ['sherly','sharon''dharshini''john']
num_students = int(input('enter number of students:'))
student_list = []
white_list = []
for student in range(num_students):
    prompt = input('input a name:')
    while prompt == '':
        prompt = input('input  non-empty name:')
    student_list.append(prompt)
for student in student_list:
    if student not in black_list:
        white_list.append(student)
print('these'+str(len(white_list))+'students are alloted to graduate.')
print(*sorted(white_list), sep='\n')
