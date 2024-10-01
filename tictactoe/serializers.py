from rest_framework import serializers
from .models import *

class TicTacToeSerializer(serializers.ModelSerializer):
    class Meta:
        model = tictactoeModel
        fields = '__all__'
        depth = 1
