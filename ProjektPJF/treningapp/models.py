from django.db import models
from django.contrib.auth.models import User


class Trening(models.Model):
    Nazwa_Treningu = models.CharField(max_length=16)
    Data_Treningu = models.DateField()
    Opis = models.TextField(null=True)
    CzasTreningu = models.IntegerField()
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nazwa_Treningu