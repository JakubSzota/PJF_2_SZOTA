from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig
from traningapp.tasks import send_weekly_email


class TrainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'traningapp'

    def ready(self):
        super().ready()
        scheduler = BackgroundScheduler()
        #scheduler.add_job(send_weekly_email, 'cron', day_of_week='mon', hour=0)
        scheduler.add_job(send_weekly_email, 'interval', seconds=10)
        scheduler.start()