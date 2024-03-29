from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import TrainingForm, TrainingExerciseForm, ExerciseForm
from django.contrib.auth.decorators import login_required
from .models import Training, TrainingExercise, Exercise
from django.db.models import F

def list_of_training_for_all(request):
    trainings = Training.objects.all()
    return render(request, '../templates/list_of_training.html', {'trainings': trainings})

@login_required
def list_of_training(request):
    current_user = request.user
    trainings = Training.objects.filter(user=current_user)
    return render(request, 'list_of_training.html', {'trainings': trainings})

@login_required
def add_training(request):
    if request.method == 'POST':
        if 'add_training' in request.POST:
            training_form = TrainingForm(request.POST)
            if training_form.is_valid():
                training = training_form.save()
                training.user = request.user
                training.save()
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
    all_calories = training.all_calories if training.all_calories else 0
    if request.method == 'POST':
        exercise_form = TrainingExerciseForm(request.POST)
        if exercise_form.is_valid():
            exercise = exercise_form.save(commit=False)
            exercise.training = training
            exercise.save()
            exercise_info = Exercise.objects.get(pk=exercise.exercise_id)
            calories_for_exercise = exercise_info.calories_per_one * exercise.series * exercise.repetitions
            all_calories += calories_for_exercise
            training.all_calories = all_calories
            training.save()

            if 'add_next' in request.POST:
                return redirect('add_exercises', training_id=training_id)
            elif 'finish' in request.POST:
                return redirect('list_of_training')
    else:
        exercise_form = TrainingExerciseForm()

    return render(request, 'add_exercises.html', {'exercise_form': exercise_form, 'training': training})
def training_exercises(request, training_id):
    training_exercises = TrainingExercise.objects.filter(training_id=training_id)
    training_name = training_exercises.first().training.name
    return render(request, 'training_exercises.html', {'training_exercises': training_exercises, 'training_name': training_name})

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_list.html', {'exercises': exercises})

def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('exercise_list'))
    else:
        form = ExerciseForm()
    return render(request, 'exercise_create.html', {'form': form})

