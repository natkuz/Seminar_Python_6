# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int(input('Enter size of list: '))

# БЫЛО
# my_list = []
# for _ in range(n):
#     my_list.append(round(random.uniform(1, 10), 2))

# СТАЛО
my_list = [round(random.uniform(1, 10), 2) for _ in range(n)]

print(f'Generated list: {my_list}')

# БЫЛО
# for i in range(len(my_list)):
#     my_list[i] = int(my_list[i] * 100 % 100)

# СТАЛО
# for i, item in enumerate(my_list):
#     my_list[i] = int(my_list[i] * 100 % 100)

my_list = [int(my_list[i] * 100 % 100) for i, item in enumerate(my_list)]

max_el = my_list[0]
i = 0
for i in range(len(my_list)):
    if my_list[i] > max_el:
        max_el = my_list[i]
    i += 1

min_el = my_list[0]
i = 0
for i in range(len(my_list)):
    if my_list[i] < min_el and my_list[i] != 0:
        min_el = my_list[i]
    i += 1

print(f'Difference between max and min value of the fractional part of the elements other than 0 = {(max_el - min_el) / 100}')