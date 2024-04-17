from django.contrib import admin

# Register your models here.
from .models import Pokemon, Caught

admin.site.register(Pokemon)
admin.site.register(Caught)