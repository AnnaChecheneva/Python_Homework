print("1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
# print("1 метод")

# N = float(input("enter N--> "))
# Ost = N - int(N)
# sum = 0
# print("Остаток:", round(Ost, 3))
# while (N != 0): 
#     sum = sum + (int(N) % 10)
#     N = N / 10
# while (Ost > 0.1): 
#     sum = sum + int(Ost*10) 
#     Ost = Ost * 10 - int(Ost * 10)
# print("Сумма цифp числа-->",sum)

# s = input(" ")
 
print("2 метод")

a = str(input("enter value:"))
print(a)
my_list=list(a)
print(list(a))
if "." in my_list:
    index_a = a.find(".")
    print(a[index_a])
    my_list.remove(".")
    print(my_list)
    print(sum(map(int, my_list)))
    
else:
    print(sum(map(int, my_list)))
s = input(" ")


print("2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.")

import math
N = int(input("Введите размер списка: "))
list_ = list(range(1, N+1))
print("Факториал числа", N,"---->",  math.prod(list_))
s = input(" ")

print("3. Задайте список из n чисел последовательности $ (1+\frac 1 n)^n $ и выведите на экран их сумму.")
# Возможно так написать код?????????

# N = float(input("Enter N--> "))
# list_ = list((range(((1+1/1)**1, (1+1/(N+1)**(N+1))))))
# print(float(list_))


N = int(input("Enter N---> "))
listik = [round((1+1/i)**i, 4) for i in range(1, N+1)]
print(listik)
print("Сумма значений списка:", sum(map(float, listik)))
s = input(" ")

print("4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.")

from random import randint
A = int(input("Enter A---> "))
listok = [randint(-A,A) for i in range(N)]
listok_mult = 1
print(listok)

with open('num.txt', 'r') as file:
    arr = file.readlines()
    for i in range(len(arr)):
        listok_mult = listok_mult * int(listok[int(i)])
print(" Произведение элементов на указанных позициях ( позиции хранятся в файле file.txt) --->", listok_mult)
s = input(" ")


print("5 Реализуйте алгоритм перемешивания списка.")
import random
listA = ['a', 'b', 'c', 'd', 'e'] 
print(listA)
random.shuffle(listA)
print(listA)
