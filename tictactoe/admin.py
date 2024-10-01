from django.contrib import admin
from .models import tictactoeModel

# Register your models here.
@admin.register(tictactoeModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'player', 'action', 'board', 'winner', 'terminal', 'time']
