from django.db import models
from django.contrib.auth.models import User

class BodyPart(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    calories_per_one = models.FloatField()
    body_part = models.ForeignKey(BodyPart, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Training(models.Model):
    name = models.CharField(max_length=100,null=True)
    datetime = models.DateTimeField()
    executed = models.BooleanField(default=False)
    all_calories = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)
    duration = models.FloatField(null=True)
    exercises = models.ManyToManyField('Exercise', through='TrainingExercise')

    def __str__(self):
        return f"Training at {self.datetime}"

class TrainingExercise(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField(default=1)
    series = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.training} - {self.exercise} - Series: {self.series}"