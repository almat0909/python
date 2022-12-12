# Пользователь вводит строку text. Реализуйте функцию, которая запрашивает у пользователя, куда он хочет сохранить эту строку: вводится последовательность папок и имя файла (расширение .txt). Затем в этот файл сохраняется значение переменной text. Если этот файл уже существует, то нужно спросить у пользователя, действительно ли он хочет перезаписать его.

# Обеспечьте контроль ввода: указанный из папок путь должен существовать на диске.

import os

text = input("Введите строку: ")

save_document = input("Куда хотите сохранить документ? Введите последовательность папок (через /):")
    #что делать если имя пользователя через пробел? Almat Ashimbayev

path = os.path.join('C:', os.path.sep, save_document)
file_name = 'my_document'#input("Введите имя файла: ")
if file_name in os.listdir(path):
    rewrite = input("Вы действительно хотите перезаписать файл? ")
    if rewrite == 'да':
        new_file = open(os.path.join(path, file_name), "w", encoding="utf8")
        new_file.write(text)
        new_file = open(os.path.join(path, file_name), "r", encoding="utf8")

        print("Содержимое файла:", new_file.read())
        print("Файл успешно перезаписан!")
        new_file.close()
else:
    new_file = open(os.path.join(path, file_name), "w", encoding="utf8")
    new_file.write(text)
    print("Файл успешно сохранён!")
    new_file = open(os.path.join(path, file_name), "r", encoding="utf8")
    print("Содержимое файла:", new_file.read())
    new_file.close()




