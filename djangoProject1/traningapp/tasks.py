from django.core.mail import send_mail
from django.utils import timezone

def send_weekly_email():
    one_week_ago = timezone.now() - timezone.timedelta(days=7)
    from django.contrib.auth.models import User
    users = User.objects.all()
    for user in users:
        subject = 'Tygodniowe podsumowanie'
        message = f'Cześć, {user.username},\nTwoje podsumowanie treningu:\n'
        send_mail(subject, message, 'aplikacjapjf@o2.pl', [user.email])
