# Ввести строку с клавиатуры Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку “Need more!”
# Если длина строки равна 5 - вывести строку “It is five”
# a = input('Введите текст ')
# if len(a) == 5:
#     print('It is fine')
# elif len(a) < 5:
#     print('Need more')
# else:
#     print(a)

# Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
# list1 = [4, 6, 5, 7, 1, 2]
# total = 0
# for i in list1:
#     if i > 3:
#         total = total + i
# print(total)

# Получить сумму кубов натуральных чисел от n до m используя цикл for
# n = 1
# m = 3
# total = 0
# for i in range(n, m+1):
#     total = total + (i ** 3)
# print(total)

# Ввести два целых числа A и B ( A < B ).
# Вывести в порядке возрастания все целые числа, расположенные между A и B
# (включая сами числа A и B ), а также количество N этих чисел
# a = int(input('Введите целое число а = '))
# b = int(input('Введите целове число b = '))
a = 1
b = 3
print(list(range(a, b)))
for i in list(range(a, b+1)):
    print(i, end='; ')