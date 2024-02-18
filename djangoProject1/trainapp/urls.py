from django.urls import path
from .views import list_of_training, add_training, add_exercises, training_exercises, exercise_list, exercise_create

urlpatterns = [
    path('list_of_training/', list_of_training, name='list_of_training'),
    path('add_training/', add_training, name='add_training'),
    path('add_exercises/<int:training_id>/', add_exercises, name='add_exercises'),
    path('training_exercises/<int:training_id>/', training_exercises, name='training_exercises'),
    path('exercise_list/', exercise_list, name='exercise_list'),
    path('exercise_create/', exercise_create, name='exercise_create'),

]
