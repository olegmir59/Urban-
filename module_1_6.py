# Практическое задание по теме: "Словари и множества"

my_dict = {"Oleg": 1959, "Vera": 1979, "Sasha":2009,"Yaroslav":2013, 'leo':2017}
print("Словарь: ", my_dict)
print("Вера родилась       в ", my_dict["Vera"], "году")
print("Отсутствующий  Вова в ", my_dict.get("Vova"), "году")  # ключ "Vova" отсутствует в словаре
my_dict["Lida"] = 1982
my_dict["Olga"] = 1983
print("Удалено значение:     ", my_dict.pop('leo'))
print("Изменённый Словарь: ",my_dict)

my_set = {2, 3, 2, 3, 2, 7.8, 7.8, "aaa", "ddd","aaa"}
print()
print("Множество           : ", my_set)
my_set.add("Кот")
my_set.add("Пёс")
my_set.remove("ddd")
print("Изменённое Множество: ", my_set)