from rest_framework import serializers
from .models import WindData

class WindDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindData
        fields = ['id', 'name', 'speed', 'direction', 'created_at']