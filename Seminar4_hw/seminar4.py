print("1.Вычислить число c заданной точностью d")
a = float(input("Введите любое число---> "))
d = (input("Введите точность округления---> "))
print(f'{a:.{d}f}')

print("2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")
N = int(input())
list_Simple_Mult = []
Diff = 2
while N > 1:
    if N % Diff == 0:
        list_Simple_Mult.append(Diff)
        N /=Diff
    else:
        Diff += 1
print(list_Simple_Mult)

print(" Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.")
import random
N = int(input("Задайте размерность списка---> "))
items = list(range(20))
random.shuffle(items)
print("Список с уникальными числами:", items[:N])  


print("Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.")

import random
from random import randint
import itertools

def write_file(st):
    with open('file.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_polinome(k):
    lst = [rnd() for i in range(k+1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_polinome(k)
write_file(create_str(koef))

# k = randint(2, 5)

# ratios = create_polinome(k) 
# polynom2 = create_str(k, ratios)
# print(polynom2)

# with open('file.txt', 'w') as data:
#     data.write(polynom2)