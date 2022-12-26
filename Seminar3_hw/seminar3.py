print("1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.")


def SumNonEvenNumbers(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    print(f"Сумма равна: {sum}")


lst = list(map(int, input("Введите числа через пробел:\n").split()))
SumNonEvenNumbers(lst)

print("2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.")

def multiply(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)


lst = list(map(int, input("Введите числа через пробел:\n").split()))
multiply(lst)


print("3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.")

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
diff = int(max(lst)) - int(min(lst))
print("Pазница между максимальным и минимальным значением дробной части элементов --->", int(diff))

print("4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.")

number = int(input("Введите число:"))
result = bin(number)
print(result)

print(" 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.")

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
print(fibonacci(n))
