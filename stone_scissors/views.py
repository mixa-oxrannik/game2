from .forms import ChoiceForm
from django.shortcuts import render, redirect
import random
from .models import Choice


def first(request):
    list_values = ['Камень', 'Ножницы', 'Бумага']
    value = list_values[random.randint(0, 2)]
    a = Choice.objects.all()
    selected_choice = request.GET.get('selected_choice', None)
    '''Вычисление победителя'''
    if value == selected_choice:
        result = 'Ничья'
    elif (value == list_values[0] and selected_choice == list_values[1]) or (value == list_values[1] and selected_choice == list_values[2]) or (value == list_values[2] and selected_choice == list_values[0]):
        result = 'Победа! Ты самый умный игратор в цу-е-фа!'
    else:
        result = 'Ты проиграл, лох! хехе'
    return render(request, 'index.html', {'value': value, 'a': a, 'selected_choice': selected_choice, 'result': result})

def my_choise(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            selected_choice = request.POST.get('choice', None)
            return redirect('/?selected_choice={}'.format(selected_choice))
    else:
        form = ChoiceForm()
    return render(request, 'my_choice.html', {'form': form})




