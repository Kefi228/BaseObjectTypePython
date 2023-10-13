list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_players = len(list_players)

# TODO Разделите участников на две команды

print(list_players[:int(count_players / 2)])
print(list_players[int(count_players / 2):])
