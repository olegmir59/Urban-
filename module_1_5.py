# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = (7,'text',9.0, True)
print("Неизменяемый Кортеж: ", immutable_var)
# строка immutable_var[2] = 15    вызовет ошибку    TypeError: 'tuple' object does not support item assignment, поскольку tuple неизменяемая коллекция
mutable_list = [23,'text', True]

mutable_list[1] = [23,'text', True]
mutable_list[0] = '????'
mutable_list[2] = 'Изменен !!!!'
print("Изменяемый Список:", mutable_list)