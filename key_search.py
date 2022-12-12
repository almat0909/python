# Пользователь вводит искомый ключ. Если он хочет, то может ввести максимальную глубину — уровень, до которого будет просматриваться структура. 

# Напишите функцию, которая находит заданный пользователем ключ в словаре и выдаёт значение этого ключа на экран. 

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def key_search(main_dict, search_key, max_depth=0, depth_search=False):
    if depth_search == True and max_depth <= 1:
        return None
    if search_key in main_dict:
        return main_dict[search_key]
    result = None
    for key, value in main_dict.items():
        if isinstance(value, dict):
            result = key_search(value, search_key)
            if result:
                return result

search_key = input("Искомый ключ: ")
answer = input("Хотите ввести максимальную глубину? Y/N: ").lower()

if answer == "y":
    depth = int(input("Введите глубину поиска: "))
    print(f'Значение ключа: {key_search(site, search_key, max_depth=depth, depth_search=True)}')

elif answer == "n":
    print(f'Значение ключа: {key_search(site, search_key)}')