from django.contrib import admin
from .models import Trening
from .models import Excercise
from .models import Member
# Register your models here.
admin.site.register(Trening)
admin.site.register(Excercise)
admin.site.register(Member)
