# максимум из трёх чисел
# Определение наибольшего числа, не используя при этом условных операторов, циклов и встроенную функцию max.

def num_max(num_1, num_2, num_3):
    max_num_1_2 = (num_1 + num_2 + abs(num_1 - num_2)) // 2
    return (num_3 + max_num_1_2 + abs(num_3 - max_num_1_2)) // 2


num_1_user = float(input('Цифра 1 = '))
num_2_user = float(input('Цифра 2 = '))
num_3_user = float(input('Цифра 3 = '))

print(f'Максимальная цифра = {num_max(num_1_user, num_2_user, num_3_user)}')