# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input("Введите номер четверти координатной плоскости: "))

if 1 <= number <= 4:
    if number == 1:
        print("диапазон возможных координат точек: \n x = от 0 до бесконечности \n y = от 0 до бесконечности")
    elif number == 2:
        print("диапазон возможных координат точек: \n x = от 0 до минус бесконечности \n y = от 0 до бесконечности")
    elif number == 3:
        print("диапазон возможных координат точек: \n x = от 0 до минус бесконечности \n y = от 0 до минус бесконечности")
    elif number == 4:
        print("диапазон возможных координат точек: \n x = от 0 до бесконечности \n y = от 0 до минус бесконечности")
else:
    print("Введённое число не является номером четверти координатной плоскости.")