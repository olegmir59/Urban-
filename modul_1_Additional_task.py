# Дополнительное практическое задание по модулю*
# Задание "Средний балл":
dict = {}
grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list =list(students)
students_list.sort()
for i in range(len(students_list)):
    # print(students_list[i],end=':')
    sum_gr =sum(grades[i])/len(grades[i])
    # print(sum_gr)
    dict[students_list[i]] = sum_gr

print(dict)