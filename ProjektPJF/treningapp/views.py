from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import AddTrening
from .models import Trening

# Create your views here.
def ListOfTerenning(request):
    trenings = Trening.objects.all()

    return render(request, "listTrening.html", {'trenings': trenings})

@login_required
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
