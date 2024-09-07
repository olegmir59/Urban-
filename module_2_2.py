# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
# Задача "Все ли равны?":

first, second, third =  map(int,input('Введите три целых числа через пробел: ').split())
print(first, second, third)
if (first == second  and first == third and second  == third):
    print(3)
elif(first != second  and first != third and second  != third):
    print(0)
else:
    print(2)