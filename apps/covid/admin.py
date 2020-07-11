from django.contrib import admin
from apps.covid.models import *

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Labatorista)
admin.site.register(MINSAL)