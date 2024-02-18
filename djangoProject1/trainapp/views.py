from django.shortcuts import render, redirect
from .models import Training, TrainingExercise

def list_of_training(request):
    trainings = Training.objects.all()
    return render(request, '../templates/list_of_training.html', {'trainings': trainings})

from django.shortcuts import render, redirect
from .forms import TrainingForm, TrainingExerciseForm
from .models import Training

def add_training(request):
    if request.method == 'POST':
        if 'add_training' in request.POST:
            training_form = TrainingForm(request.POST)
            if training_form.is_valid():
                training = training_form.save()
                return redirect('add_exercises', training_id=training.id)
        elif 'add_exercises' in request.POST:
            training_id = request.POST.get('training_id')
            training = Training.objects.get(pk=training_id)
            exercise_form = TrainingExerciseForm(request.POST)
            if exercise_form.is_valid():
                exercise = exercise_form.save(commit=False)
                exercise.training = training
                exercise.save()
                return redirect('list_of_training')
    else:
        training_form = TrainingForm()
    return render(request, 'add_training.html', {'training_form': training_form})

def add_exercises(request, training_id):
    training = Training.objects.get(pk=training_id)
    if request.method == 'POST':
        exercise_form = TrainingExerciseForm(request.POST)
        if exercise_form.is_valid():
            exercise = exercise_form.save(commit=False)
            exercise.training = training
            exercise.save()
            if 'add_next' in request.POST:
                return redirect('add_exercises', training_id=training_id)
            elif 'finish' in request.POST:
                return redirect('list_of_training')
    else:
        exercise_form = TrainingExerciseForm()
    return render(request, 'add_exercises.html', {'exercise_form': exercise_form, 'training': training})

def training_exercises(request, training_id):
    training_exercises = TrainingExercise.objects.filter(training_id=training_id)
    training_name = training_exercises.first().training.name  # Pobieramy nazwę treningu
    return render(request, 'training_exercises.html', {'training_exercises': training_exercises, 'training_name': training_name})