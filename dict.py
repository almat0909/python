# Напишите программу, которая выполняет следующий алгоритм действий:

# Вывести списки ключей и значений словаря.
# В “ETH” добавить ключ “total_diff” со значением 100.
# Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
# Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
# Внутри "sec_token_info" изменить название ключа “price” на “total_price”.

data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print('\nЗадача 1. Вывести списки ключей и значений словаря.')
print(f'key list: {data.keys()}')
print(f'value list: {data.values()}')
print(f'key & value list: {data.items()}')


print('\nЗадача 2. В “ETH” добавить ключ “total_diff” со значением 100.')
data.get("ETH")['total_diff'] = 100
print(data.get("ETH"))


print('\nЗадача 3. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.')
data.get("tokens")[0].get('fst_token_info')['name'] = 'dodge'
print(data.get("tokens")[0].get('fst_token_info')['name'])


print('\nЗадача 4. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.')
data.get("ETH")['totalOut'] = data.get("tokens")[1].pop('total_out')
print(data.get("ETH")['totalOut'])


print('\nЗадача 5. Внутри "sec_token_info" изменить название ключа “price” на “total_price”.')
data.get("tokens")[1].get('sec_token_info')['total_price'] = data.get("tokens")[1].get('sec_token_info').pop('price')
print(data.get("tokens")[1].get('sec_token_info')['total_price'])
print(data.get("tokens")[1].get('sec_token_info'))



