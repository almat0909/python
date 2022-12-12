# Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур, с нумерацией. 

# В первой строке нужно вывести в файл second_tour.txt количество участников второго тура. Затем программа должна вывести фамилии, инициалы и количество баллов всех участников, прошедших во второй тур, с нумерацией. Имя нужно сократить до одной буквы. Список должен быть отсортирован по убыванию набранных баллов.

# Пример:

# Содержимое файла first_tour.txt:
# 80
# Ivanov Serg 80
# Segeev Petr 92
# Petrov Vasiliy 98
# Vasiliev Maxim 78

# Содержимое файла second_tour.txt:
# 2
# 1) V. Petrov 98
# 2) P. Sergeev 92


first_file = open("first_tour.txt", "w", encoding="utf8")
first_file.write("80\n"
                 "Ivanov Serg 80\n"
                 "Segeev Petr 92\n"
                 "Petrov Vasiliy 98\n"
                 "Vasiliev Maxim 78")

print("Содержимое файла first_tour.txt:")
first_file = open("first_tour.txt", "r", encoding="utf8")
print(first_file.read())


first_file = open("first_tour.txt", "r", encoding="utf8")

second_file = open("second_tour.txt", "w", encoding="utf8")


l, k, seq = 0, 0, 0
info_list = []
for line in first_file:
    line_list = []
    l += 1
    if l == 1:
        k = int(line)
    elif l > 1:
        info = line.split()
        if int(info[2]) > k:
            seq += 1
            line_list.append((info[1][0], info[0], info[2]))
            info_list.append(line_list)
            # second_file = open("second_tour.txt", "a", encoding="utf8")

            # second_file.write(f"{seq}) {info[1][0]}. {info[0]} {info[2]}\n")


for i in range(len(info_list)):
    for j in range(i + 1, len(info_list)):
        if info_list[i][0][2] < info_list[j][0][2]:
            info_list[0], info_list[1] = info_list[1], info_list[0]

second_file = open("second_tour.txt", "a", encoding="utf8")
second_file.write(str(len(info_list)))
for i in range(len(info_list)):
    second_file.write(f"\n{i + 1}) {info_list[i][0][0]}. {info_list[i][0][1]} {info_list[i][0][2]}")


second_file = open("second_tour.txt", "r", encoding="utf8")

print("\nСодержимое файла second_tour.txt:")
print(second_file.read())

first_file.close()
second_file.close()

