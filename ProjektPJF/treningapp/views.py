from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AddTrening, AddExcercise
from .models import Trening
from .models import Excercise
# Create your views here.
def ListOfTerenning(request):
    trenings = Trening.objects.all()

    return render(request, "listTrening.html", {'trenings': trenings})

def home(request):
    return render(request, 'home.html')
def add_trening(request):
    if request.method == 'POST':
        form = AddTrening(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddTrening()

    context = {
        'form': form,
    }
    return render(request, 'add_trening.html', context)

def add_exercise(request):
    if request.method == 'POST':
        form = AddExcercise(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddExcercise()

    context = {
        'form': form,
    }
    return render(request, 'add_exercise.html', context)

def join(request):
    return render(request, 'join.html', {})
