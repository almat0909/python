# Программа получает на вход N количество человек в генеалогическом древе. Далее следует N − 1 строк, в каждой из которых задаётся родитель для каждого элемента дерева, кроме родоначальника. Каждая строка имеет вид «имя_потомка имя_родителя».

# Программа должна вывести список всех элементов древа в лексикографическом порядке (по алфавиту). После вывода имени каждого элемента необходимо вывести его высоту.

n_person = int(input("Введите количество человек: "))

parent_dict = dict()
person_set = set()

for i_pair in range(n_person - 1):
    child, parent = input(f"{i_pair + 1}-я пара: ").split()
    parent_dict[child] = parent
    person_set.add(child)
    person_set.add(parent)

result_dict = dict()

for person in person_set:
    temp = person
    count_height = 0
    while temp in parent_dict:
        count_height += 1
        temp = parent_dict[temp]
    result_dict[person] = count_height

print("\n«Высота» каждого члена семьи:")

for name, height in sorted(result_dict.items()):
    print(f'{name}: {height}')