# Напишите программу, которая шифрует содержимое текстового файла text.txt шифром Цезаря, при этом символы первой строки файла должны циклически сдвигаться на один, второй строки — на два, третьей строки — на три и так далее. Результат выведите в файл cipher_text.txt.

# Пример:

# Содержимое файла text.txt:
# Hello
# Hello
# Hello
# Hello

# Содержимое файла cipher_text.txt:
# Ifmmp
# Jgnnq
# Khoor
# Lipps

alphabet_upper = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
alphabet_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]

file_name = open("text.txt", "w", encoding="utf8")
for _ in range(4):
    file_name.write("Hello\n")

file_name = open("text.txt", "r", encoding="utf8")
print("Содержимое файла text.txt:")
print(file_name.read())

file_name = open("text.txt", "r", encoding="utf8")

shift = 0
for line in file_name:
    cipher_line = []
    shift += 1
    for sym in line:
        if sym in alphabet_lower:
            cipher_index = (alphabet_lower.index(sym) + shift) % len(alphabet_lower)
            cipher_line.append(alphabet_lower[cipher_index])
        elif sym in alphabet_upper:
            cipher_index = (alphabet_upper.index(sym) + shift) % len(alphabet_upper)
            cipher_line.append(alphabet_upper[cipher_index])
        else:
            cipher_line.append(sym)
    cipher_text = open("cipher_text.txt", "a", encoding="utf8")
    cipher_text.write(''.join(cipher_line))

cipher_text = open("cipher_text.txt", "r", encoding="utf8")
print("Содержимое файла cipher_text.txt:")
print(cipher_text.read())

file_name.close()
cipher_text.close()


