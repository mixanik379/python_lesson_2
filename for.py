# Цикл for ----------------
# ---------------------------

# Простейший for
for i in range(10):  # range(start, stop, step)
    print(i)
    if i == 5: break

for i in range(10):
    answer = input('Какая лучшая марка автомобиля?')
    if answer == 'Volvo':
        print('Вы абсолютно правы')
        break
for i in range(10):  # range(start, stop, step)
    if i == 9: break
    if i < 3: continue
    else:   print(i)




# answer = None
#
# while answer != 'Volvo':
#     answer = input('Какая лучшая марка автомобиля?')
# print('Вы абсолютно правы')
#
# while i < 10:
#     print(i)
#     i = i + 1
#     if i == 9: break
#     if i < 2: continue