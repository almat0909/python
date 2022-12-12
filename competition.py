# Здравствуйте! Мы собираемся устраивать соревнования по [данные засекречены] и хотим, чтобы вы написали эффективную программу, которая составляла бы нам протокол и определяла победителя и призёров. О логике работы программы ниже.

# Правила соревнований

# Участники имеют право играть несколько раз. Количество попыток одного участника не ограничивается.
# Окончательный результат участника определяется по одной игре, лучшей для этого участника.
# Более высокое место в соревнованиях занимает участник, показавший лучший результат.
# При равенстве результатов более высокое место занимает участник, раньше показавший лучший результат.

def max_scores(max_dict):
    player_dict = dict()
    name_set = list({max_dict[i + 1][0] for i in range(len(max_dict))})
    for i_name in range(len(name_set)):
        score = [(key, max_dict[key][1]) for key in range(1, len(max_dict) + 1) if name_set[i_name] == max_dict[key][0]]
        for i in range(len(score)):
            for j in range(i, len(score)):
                if score[i][1] < score[j][1]:
                    score[i], score[j] = score[j], score[i]
                elif score[i][1] == score[j][1]:
                    if score[i][0] > score[j][0]:
                        score[i], score[j] = score[j], score[i]

        player_dict[name_set[i_name]] = score[0]
        score = []

    return player_dict

def desc_sort(sort_dict):
    sort_list = []
    for name, score in sort_dict.items():
        sort_list.append((name, score))
    for i in range(len(sort_list)):
        for j in range(i, len(sort_list)):
            if sort_list[i][1][1] < sort_list[j][1][1]:
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
            elif sort_list[i][1][1] == sort_list[j][1][1]:
                if sort_list[i][1][0] > sort_list[j][1][0]:
                    sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    return sort_list[:3]

n_record = int(input("Сколько записей вносится в протокол? "))

print("Записи (результат и имя):")

res_players = dict()

for i_rec in range(n_record):
    result, gamer = input(f"{i_rec + 1}-я запись: ").split()
    res_players[i_rec + 1] = [gamer, int(result)]

player_max_score = max_scores(res_players)
winners = desc_sort(player_max_score)

print('\nИтоги соревнований:')
for i_place in range(3):
    print(f"{i_place + 1}-е место. {winners[i_place][0]} ({winners[i_place][1][1]})")





# res_players = {1: ['Jack', 69485], 2: ['qwerty', 95715], 3: ['Alex', 95715], 4: ['M', 83647], 5: ['qwerty', 197128], 6: ['Jack', 95715], 7: ['Alex', 93289], 8: ['Alex', 95715], 9: ['M', 95715]}
