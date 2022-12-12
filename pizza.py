# На вход в программу подаётся N заказов. Каждый заказ представляет собой строку вида «Покупатель — название пиццы — количество заказанных пицц». Реализуйте код, который выводит список покупателей и их заказов по алфавиту. Учитывайте, что один человек может заказать одно и то же несколько раз.


n_order = int(input('Введите количество заказов: '))

name_set = set()
order_dict = dict()

for i in range(n_order):
    in_dict = dict()
    order = input(f'{i + 1}-й заказ: ').split()
    name_set.add(order[0])
    in_dict[order[0]] = [order[1], order[2]]
    order_dict[i + 1] = in_dict

order_by_name_dict = dict()

for name in name_set:
    pizza_dict = dict()
    for i in order_dict:
        for key_names in order_dict.get(i).keys():
            if name == key_names:
                pizza = order_dict.get(i).get(name)[0]
                quantity = order_dict.get(i).get(name)[1]
                if pizza in pizza_dict:
                    pizza_dict[pizza] = int(pizza_dict.get(pizza)) + int(quantity)
                else:
                    pizza_dict[pizza] = int(quantity)
    order_by_name_dict[name] = pizza_dict

for name, value in order_by_name_dict.items():
    print(f'\n{name}:')
    for pizza, quantity in value.items():
        print(f"{pizza}: {quantity}")
