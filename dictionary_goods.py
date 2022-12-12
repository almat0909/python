// Каждая запись второго словаря отображает, сколько и по какой цене закупалось товаров (цена указана за одну штуку).

// Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара на складе, и выводит эту информацию на экран.


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}


store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for index, good in enumerate(goods):
    quantity, total_price = [], []
    for i in range(len(store.get(goods[good]))):
        quantity.append(store.get(goods[good])[i].get("quantity"))
        total_price.append(store.get(goods[good])[i].get("quantity") * store.get(goods[good])[i].get("price"))

    print(f"{good} — {sum(quantity)} штук, стоимость {'{:,}'.format(sum(total_price)).replace(',', ' ')} kzt")
