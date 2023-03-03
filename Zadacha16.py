# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в 
# массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

lengthArray = int(input("Задайте длину массива: "))
n = int (input("Массив состоит из натуральных чисел 1..N. Ведите натуральное число N: "))
x = int (input("Введите число x: "))
listNumber = []               # создаем пустой массив
for i in range(lengthArray):  # цикл выполняется в зависимости от длины массива раз
    listNumber.append(random.randint(1,n))         # наш массив заполняется рандомным перебором от 1 до n
print(listNumber)             # вывод нашего массива на экран

counter = 0                   # создали счётчик для повторяющейся переменной x
for i in listNumber:          # перебор, сколько раз в нашем массиве
    if i == x:                # встречается число x
        counter += 1          # увеличение счётчика на +1 
print(f"Число {x} встречается в массиве {counter} раз(а)")