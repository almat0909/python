# Есть файл text.txt, который содержит текст. Напишите программу, которая выполняет частотный анализ, определяя долю каждой буквы английского алфавита в общем количестве английских букв в тексте, и выводит результат в файл analysis.txt. Символы, не являющиеся буквами английского алфавита, учитывать не нужно. 

# В файл analysis.txt выводится доля каждой буквы, встречающейся в тексте, с тремя знаками в дробной части. Буквы должны быть отсортированы по убыванию их доли. Буквы с равной долей должны следовать в алфавитном порядке.

# Пример:

# Содержимое файла text.txt:
# Mama myla ramu.

# Содержимое файла analysis.txt:
# a 0.333
# m 0.333
# l 0.083
# r 0.083
# u 0.083
# y 0.083


alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
text = "Mama myla ramu."
text_file = open('text.txt', "w")
text_file.write(text)
print("Содержимое файла text.txt:")
text_file = open('text.txt', "r")
print(text_file.read())

count_letter = 0
letter_set = set()
letter_dict = dict()

text_file = open('text.txt', "r")

for line in text_file:
    for letter in line:
        if letter.lower() in alphabet:
            count_letter += 1
            letter_set.add(letter.lower())

letter_list = [[i_letter, round(text.lower().count(i_letter) / count_letter, 3)] for i_letter in sorted(letter_set)]

for i in range(len(letter_list)):
    for j in range(i, len(letter_list)):
        if letter_list[i][1] < letter_list[j][1]:
            letter_list[i], letter_list[j] = letter_list[j], letter_list[i]


analysis_file = open('analysis.txt', "w")
for i_elem in letter_list:
    for elem in i_elem:
        analysis_file.write(str(elem))
        analysis_file.write(' ')
    analysis_file.write('\n')


print("\nСодержимое файла analysis.txt:")
analysis_file = open('analysis.txt', "r")
print(analysis_file.read())

text_file.close()
analysis_file.close()
