import random

def game_progress(selected_choice):
    '''Вычисление победителя оффлайн игры'''
    list_values = ['Камень', 'Ножницы', 'Бумага']
    value = list_values[random.randint(0, 2)]
    if value == selected_choice:
        result = 'Ничья'
    elif (value == list_values[0] and selected_choice == list_values[1]) or (
            value == list_values[1] and selected_choice == list_values[2]) or (
            value == list_values[2] and selected_choice == list_values[0]):
        result = 'Победа!'
    else:
        result = 'Проиграл:('
    return value, result

def game_total(choice1, choice2):
    '''Вычисление победителя онлайн игры'''
    list_values = ['Камень', 'Ножницы', 'Бумага']
    if choice1 == choice2:
        return 'Ничья'
    elif (choice1 == list_values[0] and choice2 == list_values[1]) or (
          choice1 == list_values[1] and choice2 == list_values[2]) or (
          choice1 == list_values[2] and choice2 == list_values[0]):
        return 'Победил: Игрок1'
    elif (choice2 == list_values[0] and choice1 == list_values[1]) or (
            choice2 == list_values[1] and choice1 == list_values[2]) or (
            choice2 == list_values[2] and choice1 == list_values[0]):
        return 'Победил: Игрок2'
    else:
        return 'Ждём действий второго игрока'
