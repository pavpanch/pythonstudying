from typing import List

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  #список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} #множество

students = list(students)
stud = students.sort()
print(type(grades))
print(students)

dict=dict(zip(students, grades))
print(dict)
a=len(grades)
sum = 0
#for i in grades[0:a]:
for i in range(a):
    b = len(grades[i])
    #s = str(grades[i])

    print('кол-во:', b)
    for j in range(b):
        l = len(grades[j])
        #summa = sum(grades[i[j]])
        s = sum(grades[j])
        print(grades[j])
        print('Cумма', s)
 #   j=len(grades[i])
  #  print(sum)

#for i in range(len(grades)):
#    for j in range(len(grades[i]):
#        print(grades[i][j], end = ' ')
#    print()