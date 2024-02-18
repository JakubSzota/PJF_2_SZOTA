from turtle import home
from django.contrib import admin
from django.urls import path, include
from treningapp.views import ListOfTerenning, add_trening, home, add_exercise, join

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listTrening/', ListOfTerenning, name='listoftrening'),
    path('AddTrening/', add_trening, name='addtrening'),
    path('AddExcercise/', add_exercise, name='addexcercise'),
    path('', home, name='home'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('join/', join , name='join'),

]
