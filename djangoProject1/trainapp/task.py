from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Training

@shared_task
def send_weekly_training_email():
    users = User.objects.all()

    for user in users:
        num_trainings = Training.objects.filter(user=user).count()

        subject = 'Weekly Training Summary'
        message = f'Hello {user.username},\n\nYou had {num_trainings} training(s) this week.\n\nBest regards,\nYour Training App'

        #send_mail(subject, message, 'your@example.com', [user.email])
        print("gfasgdfjsadhgf")