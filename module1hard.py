grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron','test'}
new_students=list(students)
new_students.sort()
print(new_students)
# Первый метод перебор циклом
# grades_2=[]
# for element_1 in grades :
#     grades_2.append(sum(element_1)/len(element_1))
# Второй использование map()   прикольный
grades_2=list(map(lambda nn:sum(nn)/len(nn),grades))
print(grades_2)
#создадим словарь  перебор в цикле не хочу пробовать длинный
# (проверил пары создаются по наличию ,грубо по короткому списку)
gurnal = dict(zip(new_students,grades_2))
print(gurnal)