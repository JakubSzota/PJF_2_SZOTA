from django.contrib import admin

from .models import Training, Exercise, TrainingExercise, BodyPart

admin.site.register(Training)
admin.site.register(Exercise)
admin.site.register(TrainingExercise)
admin.site.register(BodyPart)