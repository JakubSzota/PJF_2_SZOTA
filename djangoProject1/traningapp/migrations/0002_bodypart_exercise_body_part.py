# Generated by Django 4.2.10 on 2024-02-18 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traningapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='body_part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='traningapp.bodypart'),
        ),
    ]
