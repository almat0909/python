# При регистрации на сайте помимо логина нужно ещё придумать надёжный пароль. Этот пароль должен состоять минимум из восьми символов, в нём должны быть хотя бы одна большая буква и хотя бы три цифры. Тогда он будет считаться надёжным. 
# 
# Напишите программу, которая запрашивает у пользователя пароль до тех пор, пока он не введёт надёжный пароль. Используется латиница.

password = input('Придумайте пароль: ')

digit_list = [sym for sym in password if sym.isdigit()]
upper_list = [letter for letter in password if letter == letter.upper() and not letter.isdigit()]

if len(password) > 7 and len(digit_list) > 2 and len(upper_list) > 0:
    print('Это надёжный пароль!')
else:
    print('Пароль ненадёжный. Попробуйте ещё раз.')