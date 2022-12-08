# MyProfile app

SEPARATOR = '-'*42

# personal information
name = str()
age = int()
phone = str()
email = str()
index = str() # digits are saved only
post_address = str()
additional_info = str()

# entrepreneur information
msrnie = int() # 15 digits
iin = int()
check_account = int() # 20 digits
bank_name = str()
bik = int()
correspondent_account = int()


def personal_info(name, age, phone, email, index, post_address, additional_info):
    print(SEPARATOR)
    print('Имя:', name)
    if 11 <= age % 100 <= 19:
        years_parameter = 'лет'
    elif age % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age, years_parameter)
    print('Телефон:', phone)
    print('E-mail:', email)
    if index:
        print('Почтовый индекс:', index)
    print('Адрес:', post_address)
    if additional_info:
        print('Дополнительная информация:', additional_info)

def entrepreneur_info(name, age, phone, email, index, post_address, additional_info, msrnie, iin, check_account, bank_name, bik, correspondent_account):
    print(SEPARATOR)
    print('Имя:', name)
    if 11 <= age % 100 <= 19:
        years_parameter = 'лет'
    elif age % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', age, years_parameter)
    print('Телефон:', phone)
    print('E-mail:', email)
    print('E-mail:', index)
    print('Адрес:', post_address)
    if additional_info:
        print('Дополнительная информация:', additional_info)

    print('\nИнформация о предпринимателе')
    print('ОГРНИП:', msrnie)
    print('ИИН:', iin)
    print('Банковские реквизиты')
    print('Расчетный счет:', check_account)
    print('Банк:', bank_name)
    print('БИК:', bik)
    print('К/с:', correspondent_account)


print('Приложение MyProfile для предпринимателей')

while True:
    # main menu
    print(f'{SEPARATOR}'
          f'\nГЛАВНОЕ МЕНЮ'
          f'\n1 - Ввести или обновить информацию'
          f'\n2 - Вывести информацию'
          f'\n0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(f'{SEPARATOR}'
                  f'\nВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ'
                  f'\n1 - Личная информация'
                  f'\n2 - Информация и предпринимателе'
                  f'\n0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while True:
                    # validate user age
                    while True:
                        try:
                            age = int(input('Введите возраст: '))
                            break
                        except ValueError:
                            print('Возраст должен быть целым числом')

                    if 0 < age < 150:
                        break
                    elif age < 0:
                        print('Возраст должен быть положительным')
                    elif age > 150:
                        print('Такой возраст маловероятен')

                while True:
                    # validate phone number
                    phone_input = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                    phone = str()
                    for item in phone_input:
                        if item == '+' or ('0' <= item <= '9'):
                            phone += item
                    if len(phone) != 12:
                        print('Формат телефона должен быть: +7ХХХХХХХХХХ')
                    else:
                        break
                while True:
                    email = input('Введите адрес электронной почты: ')
                    if '@' and '.' in email:
                        break
                    else:
                        print('Электронная почта должна содержать . и @')

                index_input = input('Введите почтовый индекс: ')
                index = str()
                for item in index_input:
                    if item in '0123456789':
                        index += item

                post_address = input('Введите почтовый адрес (без индекса): ')
                additional_info = input('Введите дополнительную информацию: ')

            elif option2 == 2:
                # input entrepreneur information
                while True:
                    msrnie = input('Введите ОГРНИП: ')
                    if len(msrnie) == 15:
                        digit_count = str()
                        for item in msrnie:
                            if item in '0123456789':
                                digit_count += item
                        if len(digit_count) == 15:
                            break
                    else:
                        print('ОГРНИП должен сожержать 15 цифр')

                while True:
                    try:
                        iin = int(input('Введите ИИН: '))
                        break
                    except ValueError:
                        print('ИИН должен содержать только цифры')

                while True:
                    check_account = input('Введите расчетный счет: ')
                    if len(check_account) == 20:
                        digit_count = str()
                        for item in check_account:
                            if item in '0123456789':
                                digit_count += item
                        if len(digit_count) == 20:
                            break
                    else:
                        print('Расчетный счет должен сожержать 20 цифр')
                bank_name = input('Введите название банка: ')

                while True:
                    try:
                        bik = int(input('Введите БИК: '))
                        break
                    except ValueError:
                        print('БИК должен содержать только цифры')

                while True:
                    try:
                        correspondent_account = int(input('Введите корреспондентский счет: '))
                        print(correspondent_account)
                        break
                    except ValueError:
                        print('К/с должен содержать только цифры')


            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(f'{SEPARATOR}'
                  f'\nВЫВЕСТИ ИНФОРМАЦИЮ'
                  f'\n1 - Общая информация'
                  f'\n2 - Вся информация'
                  f'\n0 - Назад'
                  f'\n{SEPARATOR}')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # print personal information
                personal_info(name, age, phone, email, index, post_address, additional_info)

            elif option2 == 2:
                # print entrepreneur information
                entrepreneur_info(name, age, phone, email, index, post_address, additional_info, msrnie, iin, check_account, bank_name, bik, correspondent_account)

            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')