students = {"Harry": 37.21, "Berry": 37.21, "Tina": 37.2, "Akriti": 41, "Harsh": 39}
grades = [37.21, 37.21, 37.2, 41, 39]

students_to_print = []

second_last = sorted(set(grades))[1]

for student in students:
    if second_last == students[student]:
        students_to_print.append(student)

for i in sorted(students_to_print):
    print(i)


# Outra solução

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))