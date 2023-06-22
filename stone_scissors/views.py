import asyncio
import websockets

from django.shortcuts import render, redirect

from .models import Choice
from .main import game_progress, game_total
from .forms import ChoiceForm


def result_game(request):
    '''Winner display'''
    selected_choice = request.GET.get('selected_choice', None)
    result = game_progress(selected_choice)
    return render(request, 'index.html', {'value': result[0], 'selected_choice': selected_choice, 'result': result[1]})


def my_choise(request):
    '''Offline option selection page'''
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            selected_choice = request.POST.get('choice', None)
            return redirect('/offline?selected_choice={}'.format(selected_choice))
    else:
        form = ChoiceForm()
    return render(request, 'my_choice.html', {'form': form})


def main(request):
    '''Main page'''
    chois = Choice.objects.all()
    if len(chois) < 2:
        a = 'Eщё выбирает'
    else:
        a = chois[1]
    return render(request, 'main.html', {'selected_choice': chois[0], 'enemy_choice': a})


def choice_online(request):
    '''Choosing an option in an online game'''
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            a = Choice.objects.all()
            if len(a) > 1:
                a.delete()
            selected_choice = form.cleaned_data['choice']
            choice_obj = Choice.objects.create(choice=selected_choice)
            if len(Choice.objects.all()) == 2:
                all_choice = Choice.objects.all()
                return redirect('/total_online?selected_choice={}&enemy_choice={}'.format(all_choice[0], all_choice[1]))
            enemy_choice = 'Ещё выбирает'
            return redirect('/total_online?selected_choice={}&enemy_choice={}'.format(choice_obj.choice, enemy_choice))
    else:
        form = ChoiceForm()
    return render(request, 'my_choice.html', {'form': form})


def total_online(request):
    '''Display result for 2nd player'''
    selected_choice = request.GET.get('selected_choice', None)
    enemy_choice = request.GET.get('enemy_choice', None)
    result = game_total(selected_choice, enemy_choice)
    return render(request, 'total_online.html', {'selected_choice': selected_choice, 'enemy_choice': enemy_choice, 'result': result})




# async def handle_websocket(websocket, path):
#     while True:
#         # обработка сообщений от клиента
#         message = await websocket.recv()
#         await websocket.send("You said: " + message)
#         await asyncio.sleep(5)  # добавлено ожидание
#
# async def online_connected(request):
#     return render(request, "websocket_connected.html")
#
# async def start_websocket(request):
#     async with websockets.serve(handle_websocket, "0.0.0.0", 8765):
#         await asyncio.Future()  # сервер будет работать бесконечно
#
# def websocket_connected(request):
#     loop = asyncio.get_event_loop()
#     loop.create_task(start_websocket(request))
#     return render(request, "websocket_connected.html")










