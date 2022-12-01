# Max
# из двух введённых чисел определяет наибольшее, 
# не используя при этом условных операторов, циклов и встроенную функцию max.

first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

max_num = (second_num + first_num + abs(first_num - second_num)) // 2

print(f'Наибольшее число: {max_num}')