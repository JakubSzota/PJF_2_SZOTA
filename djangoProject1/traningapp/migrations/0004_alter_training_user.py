# Generated by Django 4.2.10 on 2024-02-19 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('traningapp', '0003_training_all_calories_alter_exercise_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
