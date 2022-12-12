# Пользователь вводит строку. Напишите программу, которая определяет, является ли заданная строка правильным IP-адресом. Обеспечьте контроль ввода, где предусматривается ввод целых чисел от 0 до 255, а также точки между ними.


IP_address = input('Введите IP: ')

correct_IP = 0
for IP in IP_address.split('.'):
    if IP.isdigit() and int(IP) > 255:
        print(f'{IP} превышает 255.')

    elif not IP.isdigit():
        print(f'{IP} — это не целое число.')

    else:
        correct_IP += 1

if IP_address.count('.') != 3:
    print('Адрес — это четыре числа, разделённые точками.')

elif correct_IP == 4 and IP_address.count('.') == 3:
    print('IP-адрес корректен.')


