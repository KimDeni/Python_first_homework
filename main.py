from math import sqrt


# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# def day_of_the_week_search():
#     print("Введите номер дня недели(от 1 до 7)")
#     num = int(input())
#
#     while num < 1 or num > 7:
#         print("Введите номер дня недели(от 1 до 7)")
#         num = int(input())
#
#     if 0 < num < 6:
#         print('НЕТ')
#     else:
#         print('ДА')
#
#
# day_of_the_week_search()


# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def truth_table():
#     for X in (0, 1):
#         for Y in (0, 1):
#             for Z in (0, 1):
#                 if not (X or Y or Z) == (not X and not Y and not Z):
#                     print(f' {X}  {Y}  {Z}  {not (X or Y or Z) == (not X and not Y and not Z)} ')
#                 else:
#                     print(f'| {X}  {Y}  {Z}  {not (X or Y or Z) == (not X and not Y and not Z)} ')
#
#
# truth_table()


# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# def quarter_coordinate_search(x, y):
#     if x > 0 and y > 0:
#         print("Точка находится в 1 четверти")
#     elif x < 0 and y > 0:
#         print("Точка находится в 2 четверти")
#     elif x < 0 and y < 0:
#         print("Точка находится в 3 четверти")
#     elif x > 0 and y < 0:
#         print("Точка находится в 4 четверти")
#
#
# x = int(input("Введите координаты Х: "))
# y = int(input("Введите координаты Y: "))
#
# quarter_coordinate_search(x, y)


# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# def coordinate_range():
#     while True:
#         quarter = int(input("Введите номер четверти: "))
#         if 0 < quarter < 5:
#             if quarter == 1:
#                 print("X > 0, Y > 0")
#                 break
#             elif quarter == 2:
#                 print("X < 0, Y > 0")
#                 break
#             elif quarter == 3:
#                 print("X < 0, Y < 0")
#                 break
#             elif quarter == 4:
#                 print("X > 0, Y < 0")
#                 break
#         else:
#             print("Введите число от 1 до 4")
#
#
# coordinate_range()


# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# def distance_between_points(ax, ay, bx, by):
#     return print("Расстояние между точками: ", round((sqrt(int((bx - ax)) ** 2 + int((ay - by)) ** 2)), 2))
#
#
# ax = int(input("Введите координаты AX: "))
# bx = int(input("Введите координаты BX: "))
# ay = int(input("Введите координаты AY: "))
# by = int(input("Введите координаты BY: "))
# distance_between_points(ax, ay, bx, by)
