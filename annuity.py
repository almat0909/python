# Аннуитетный платёж
# 
# Кредит в сумме S млн руб., выданный на n лет под i% годовых, подлежит погашению равными ежегодными выплатами в конце каждого года, включающими процентные платежи и сумму в погашение основного долга. 
# Проценты начисляются в один раз в год. 
# После выплаты третьего платежа достигнута договорённость между кредитором и заёмщиком о продлении срока погашения займа на n_2 лет и увеличении процентной ставки с момента конверсии до i_2%. Напишите программу, которая выводит план погашения оставшейся части долга.
# Используйте следующие формулы (А — размер аннуитетного платежа, его дробную часть округлите до двух знаков, то есть до копеек):
# i - процент в дробном виде (6% —> 0.06)


def anniutet(credit, year, percent):
    k = (percent * (1 + percent) ** year) / ((1 + percent) ** year - 1)
    a_pay = round(k * credit, 2)

    return a_pay

def payment(credit, percent, a_payment, period):
    for i in range(period):
        print(f'\nПериод: {i + 1}')
        print(f'Остаток долга на начало периода: {credit}')
        paid_percent = round(credit * percent, 2)
        print(f'Выплачено процентов: {paid_percent}')
        paid_credit = round(a_payment - paid_percent, 2)
        print(f'Выплачено тела кредита: {paid_credit}')

        credit -= paid_credit

    return credit


credit_init = float(input("Введите сумму кредита: "))
year_init = int(input("На сколько лет выдан? "))
percent_init = int(input("Сколько процентов годовых? "))/100

a_payment = anniutet(credit_init, year_init, percent_init)
left_credit = payment(credit_init, percent_init, a_payment, 3)
print(f'\nОстаток долга: {left_credit}')

print('\n ==================== ')

new_year = int(input('На сколько лет продлевается договор? '))
new_percent = int(input("Увеличение ставки до: ")) / 100

new_year = new_year + year_init - 3
a_payment_new = anniutet(left_credit, new_year, new_percent)

print(f'\nОстаток долга: {payment(left_credit, new_percent, a_payment_new, new_year)}')
