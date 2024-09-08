#  Дополнительное практическое задание по модулю*
#  Задание "Слишком древний шифр":

n = 0
while n < 3 or n > 20:
    n = int(input("Ведите число (от 3 до 20): "))
shifr = ""
pairs_nums = ""
for i in range(1,n):
    for j in range(1,n):
        num1 = i
        num2 = j
        if num1 >= num2:
            continue
        elif n % (num1 + num2) == 0:
            shifr += str(num1) + str(num2)
            pairs_nums += str(num1) + " и " + str(num2) + ", "
print(n, " - число из первой вставки")
print(shifr + " - нужный пароль, (" + pairs_nums + "- пары; число ", n, " кратно сумме каждой пары)")