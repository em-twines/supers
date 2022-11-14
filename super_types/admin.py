from django.contrib import admin
from .models import SuperType
from supers.models import Super
# Register your models here.

admin.site.register(SuperType)
admin.site.register(Super)