# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print("1.программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.")
num_weekD = int(input("Please, enter a number day of the week---> "))
if  0 < num_weekD < 6:
    print(" it`s day for work!")
elif 6 < num_weekD < 8:
    print("Great! It`s a weekend!")
else: print("You enter a wrong number of the week. Try again:3")
print()
s = input(" ") 


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("2.программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.")


for x in 0, 1:
        for y in 0,1 :
            for z in 0,1:
                if   (not (x or y or z)) == ((not x) and (not y) and (not z)):
                    print("True")
                    print(x, y, z)
                    print()
                else:
                    print("False")
                    print(x, y, z)
                    print()
s = input(" ") 

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print("3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).")
x_coord = float(input("Coordinate x---> "))
y_coord = float(input("Coordinate y---> "))

if x_coord>0 and y_coord>0:
    print("It`s first quarter.")
elif x_coord<0 and y_coord>0:
    print("It`s second quarter.")
elif x_coord<0 and y_coord<0:
    print("It`s third quarter.")
else:
    print("It`s forth quarter.")

s = input(" ") 

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print("4.программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).")
coord_list = ["x > 0 and y > 0", "x < 0 and y > 0", "x < 0 and y < 0", "x > 0 and y < 0"]
my_quarter = int(input(" Please, enter the quarter---> "))
if coord_list[my_quarter-1] in coord_list:
    print("Range of points")
    print(coord_list[my_quarter-1] )
else:
    print("Enter the correct quarter")
s = input(" ")

# 5 Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
print("5. программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.")
import math
print("Enter Dote1:")
Dote1 = []
for i in range(2):
    Dote1.append(float(input()))
print("Coordinates Dote1:")
print(Dote1)

print("Enter Dote2:")
Dote2 = []
for i in range(2):
    Dote2.append(float(input()))
print("Coordinates Dote2:")
print(Dote2)

Dote_Distance = math.sqrt(((Dote1[0]-Dote2[0])**2) + ((Dote1[1]-Dote2[1])**2))
print("Distance")
print(Dote_Distance)