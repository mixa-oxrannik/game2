import random

def game_progress(selected_choice):
    '''Вычисление победителя'''
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