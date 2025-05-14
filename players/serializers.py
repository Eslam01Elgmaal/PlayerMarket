from rest_framework import serializers
from .models import Players

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'  # يعني هتستخدم كل الحقول اللي في الموديل
