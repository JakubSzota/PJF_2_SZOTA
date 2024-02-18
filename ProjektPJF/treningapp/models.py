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
class Excercise(models.Model):
    Nazwa_cwiczenia = models.CharField(max_length=16)
    Liczba_Serii = models.IntegerField()
    Opis = models.TextField(null=True)
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nazwa_Treningu

class Member(models.Model):
    Imie = models.CharField(max_length=16)
    Nazwisko = models.CharField(max_length=16)
    Email = models.EmailField(max_length=40)
    Wiek= models.IntegerField()

    def __str__(self):
        return self.Imie + ' ' + self.Nazwisko