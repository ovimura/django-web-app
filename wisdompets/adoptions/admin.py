from django.contrib import admin

from .models import Pet
# user: omura, pwd: learningdjango
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
