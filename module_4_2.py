#  Домашнее задание по уроку "Пространство имен"

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()         # inner_function()  видима.

inner_function()        # inner_function() не видима, видимость не снаружи, а изнутри!