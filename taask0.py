# 1.Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
import random

list1 = [random.randint(1,10) for i in range(0,10)]
print(list1)
list2 = [list1[i] for i in range(1, len(list1), 2)]
print(list2)
print(sum(list2))