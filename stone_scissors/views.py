from .forms import ChoiceForm
from django.shortcuts import render, redirect
from .models import Choice
from .main import game_progress


def first(request):
    a = Choice.objects.all()
    selected_choice = request.GET.get('selected_choice', None)
    result = game_progress(selected_choice)
    return render(request, 'index.html', {'value': result[0], 'a': a, 'selected_choice': selected_choice, 'result': result[1]})

def my_choise(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            selected_choice = request.POST.get('choice', None)
            return redirect('/?selected_choice={}'.format(selected_choice))
    else:
        form = ChoiceForm()
    return render(request, 'my_choice.html', {'form': form})




