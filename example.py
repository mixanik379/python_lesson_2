'''
# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
e = 1

while e <= 5:
    print(e,  '0')
    e = e + 1
'''

'''
# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.

sum = 0
i = 0
while sum < 10:
    number = input('Введите цифру:')
    if int(number) == 5: i += 1
    sum += 1
print("Количество введенных цифр'5'", i, 'шт.')
'''

'''
# Задача 3
# Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.

sum = 0
for i in range(1,101):
    sum+=i
print(sum)
'''

'''
# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

result = 1
for i in range(1,11):
    result *= i
print(result)
'''

'''
# Задача 5
# Вывести цифры числа на каждой строчке.

i = str(input('Введите число:'))  # Назначение для переменной "i" строчного типа данных вводимых пользователем.
print(type(i))                    # Вывод на экран текущего типа данных переменной "i".
number = i [::-1]                 # Присвоение переменной "number" данных переменной "i" и в результате действий со списком где "START" и "STOP" не указываем, указываем "STEP" "-1" получаем индексированный с конца список (например: введено 1234. 1=-3, 2=-2, 3=-1, 4=0).
print(type(number))               # Вывод на экран текущего типа данных для переменной "number".
number = int(number)              # Замена типа данных для переменной "number" со строчного "str" на числовой "int".
print(type(number))               # Вывод на экран текущего типа данных для переменной "number".
print(number)                     # Вывод состояния данных переменной "number" (для наглядности).
print()                           # Вывод пустой строки.
print('Результат представлен в прямом порядке слева на право,'
 'получен при помощи списка с шагом с конца "[::-1]".')
while number > 0:                 # Вывод списка в цикле "while". Переменная "number" больше индекса 0.
    print(number%10)              # Вывод на экран остатка от деления на 10 (числа из списка с шагом -1).
    number = number//10           # Следующий вывод на экран с делением на 10.
'''

'''
# Задача 6
# Найти сумму цифр числа.

integer_number = 56473
sum = 0
while integer_number>0:
    sum += integer_number%10
    integer_number = integer_number//10
print(sum)
'''

'''
Задача 7
Найти произведение цифр числа.
'''

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?

integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Да')
        break
    integer_number = integer_number//10
else: print('Нет')
'''

'''
# Задача 9
# Найти максимальную цифру в числе

integer_number = 1234560654321
i = 0
while integer_number>0:
    if integer_number%10 >= i:
        i = integer_number%10
    integer_number = integer_number//10
print('Максимальное число:', i)
'''

'''
# Задача 10
# Найти количество цифр 5 в числе

i = int(input('Введите число'))
e = 0
while i >0:
    last = i % 10
    if last == 5 :
        e = e + 1
    i = i // 10
print('Количество цифр 5 равно ', e, 'шт.')
'''