# Пользователь вводит текст, состоящий из слов и знаков препинания. Напишите программу, которая переворачивает (записывает в обратном порядке) все слова текста, оставив знаки препинания без изменений. Словом в тексте считается последовательность символов из прописных и строчных букв кириллицы.

def rev_text(text):
    alphabet = [chr(index) for index in range(ord('а'), ord('я') + 1)]
    alphabet_upper = [chr(index) for index in range(ord('А'), ord('Я') + 1)]
    alphabet.extend(alphabet_upper)

    cipher_text, temp = list(), list()

    for sym in text:
        if sym in alphabet:
            temp.append(sym)
        else:
            temp.reverse()
            cipher_text.extend(temp)
            cipher_text.append(sym)
            temp = list()
    return ''.join(cipher_text)

user_input = input('Сообщение: ')

print(f"Новое сообщение: {rev_text(user_input)}")