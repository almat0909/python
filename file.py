# Напишите программу, которая получает на вход путь до каталога (это может быть и просто корень диска) и выводит общее количество файлов и подкаталогов в нём. Также выведите на экран размер каталога в килобайтах (1 килобайт = 1024 байт).

# Важный момент: чтобы посчитать, сколько весит каталог, нужно найти сумму размеров всех вложенных в него файлов. 

# Результат работы программы на примере python_basic\Module14:

# E:\PycharmProjects\python_basic\Module14
# Размер каталога (в Кб): 8.373046875
# Количество подкаталогов: 7
# Количество файлов: 15


import os

count_folder, count_file = 0, 0
abs_path = os.path.abspath(os.path.join('..'))

for i_folder in os.listdir(abs_path):
    if os.path.isdir(os.path.abspath(os.path.join(abs_path, i_folder))):
        count_folder += 1
    for i_file in os.listdir(os.path.abspath(os.path.join('..', i_folder))):
        if os.path.isfile(os.path.abspath(os.path.join(abs_path, i_folder, i_file))):
            count_file += 1

print('Размер каталога (в Кб):', os.stat(abs_path).st_size)
print('Количество подкаталогов:', count_folder)
print('Количество файлов:', count_file)
