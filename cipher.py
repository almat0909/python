# К вам попал зашифрованный текст, означающий большую истину для многих программистов на Python. Напишите программу, которая реализует алгоритм дешифровки этого текста. Расшифруйте текст с помощью своей программы, а затем найдите его в интернете.

def cipher(text):
    shift = -1
    alphabet = [chr(index) for index in range(ord('a'), ord('z') + 1)]
    alphabet_upper = [chr(index) for index in range(ord('A'), ord('Z') + 1)]
    alphabet.extend(alphabet_upper)

    cipher_text = [alphabet[(alphabet.index(sym) + shift) % len(alphabet)] if sym in alphabet else sym for sym in text]

    return ''.join(cipher_text)


def shift(str_text, key):
    text = list(str_text)
    shift = key % len(str_text)
    for _ in range(shift):
        for i in range(len(text) - 1, 0, -1):
            text[i], text[i - 1] = text[i - 1], text[i]

    return ''.join(text)

user_input = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf'

result_test = []
key = 3

lst = user_input.split()
for i in range(len(lst)):
    lst[i] = lst[i].replace("+", "*")
    lst[i] = lst[i].replace("-", ",")
    lst[i] = lst[i].replace("(", "'")
    lst[i] = lst[i].replace("..", "--")
    lst[i] = lst[i].replace('"', "!")


    cipher_txt = cipher(lst[i])
    shift_txt = shift(cipher_txt, key)

    if shift_txt.endswith("/"):
        key += 1

    shift_txt = shift_txt.replace('/', ".\n")

    result_test.append(shift_txt)



print(" ".join(result_test))

