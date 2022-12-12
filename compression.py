# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на экран. Кодирование должно учитывать регистр символов.

text = input('Введите строку: ')

count = 0
cipher_text = []

for i in range(len(text)):
    count += 1
    if text[i] != text[i + 1: i + 2]:
        cipher_text.append(text[i] + str(count))
        count = 0

print(f"Закодированная строка: {''.join(cipher_text)}")