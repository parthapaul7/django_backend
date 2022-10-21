from django.contrib import admin

# Register your models here.
from .models import Country 

class ContriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'flag')

admin.site.register(Country, ContriesAdmin)
