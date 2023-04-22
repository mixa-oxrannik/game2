from .forms import ChoiceForm
from django.shortcuts import render, redirect
from .models import Choice
from .main import game_progress, game_total



def result_game(request):
    '''Отображение победителя'''
    selected_choice = request.GET.get('selected_choice', None)
    result = game_progress(selected_choice)
    return render(request, 'index.html', {'value': result[0], 'selected_choice': selected_choice, 'result': result[1]})

def my_choise(request):
    '''Страница выбора варианта для оффлайн игры'''
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            selected_choice = request.POST.get('choice', None)
            return redirect('/offline?selected_choice={}'.format(selected_choice))
    else:
        form = ChoiceForm()
    return render(request, 'my_choice.html', {'form': form})

def main(request):
    '''Главная страница'''
    return render(request, 'main.html')

def choice_online(request):
    '''Выбор варианта в онлайн игре'''
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            a = Choice.objects.all()
            if len(a) > 1:
                a.delete()
            selected_choice = form.cleaned_data['choice']
            choice_obj = Choice.objects.create(choice=selected_choice)
            if len(Choice.objects.all()) == 2:
                enemy_choice = Choice.objects.all()[0]
                return redirect('/total_online?selected_choice={}&enemy_choice={}'.format(choice_obj.choice, enemy_choice))
            return redirect('/offline?selected_choice={}'.format(choice_obj.choice))
    else:
        form = ChoiceForm()
    return render(request, 'choice_online.html', {'form': form})

def total_online(request):
    '''Отображение результата для 2-го игрока'''
    selected_choice = request.GET.get('selected_choice', None)
    enemy_choice = request.GET.get('enemy_choice', None)
    result = game_total(selected_choice, enemy_choice)
    return render(request, 'total_online.html', {'selected_choice': selected_choice, 'enemy_choice': enemy_choice, 'result': result})

def expectation_total_online(request):
    selected_choice = request.GET.get('selected_choice', None)
    return render(request, 'expectation_total_online.html', {'selected_choice': selected_choice})






