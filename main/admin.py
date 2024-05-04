from django.contrib import admin
from main.models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    display= ('name', 'surname',)
    serch_fields=('name', 'surname',)
    ordering=('name',)
    
