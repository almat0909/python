# Напишите программу, которая определяет, сколько букв (латинского алфавита), слов и строк в файле zen.txt (который содержит всё тот же Дзен Пайтона). Выведите три найденных числа на экран.

# Дополнительно: выведите на экран букву, которая встречается в тексте наименьшее количество раз.

# Обратите внимание, что регистр буквы не имеет значение. (А и а - одинаковые буквы).

# Формат вывода:

# Количество букв в файле: 
# Количество слов в файле: 
# Количество строк в файле: 
# Наиболее редкая буква: 



import os

alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]

file_from = open("zen.txt", "r", encoding="utf8")

count_line, count_letter, count_word = 0, 0, 0
letter_set = set()
letter_list = list()

for line in file_from:
    clear_line = line.rstrip()
    count_line += 1
    words = len(clear_line.split())
    count_word += words
    for letter in clear_line:
        if letter.lower() in alphabet:
            count_letter += 1
            letter_set.add(letter.lower())
            letter_list.append(letter.lower())


word_freq_dict = {i_letter: letter_list.count(i_letter) for i_letter in letter_set}
min_freq = min(word_freq_dict.values())
min_freq_letter = [key for key, value in word_freq_dict.items() if value == min_freq]


print('Количество букв в файле:', count_letter)
print('Количество слов в файле:', count_word)
print('Количество строк в файле:', count_line)
print('Наиболее редкая буква:', min_freq_letter[0])