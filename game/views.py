from django.shortcuts import render, redirect
from .models import DiceGame

def home(request):
    if request.method == 'POST':
        num_dice = int(request.POST['num_dice'])
        sides = []
        for i in range(num_dice):
            sides.append(int(request.POST[f'sides_{i+1}']))
        rolls = DiceGame.roll_dice(num_dice, sides)
        return redirect('history')
    return render(request, 'game/home.html')

def history(request):
    history = DiceGame.get_history()
    return render(request, 'game/history.html', {'history': history})
