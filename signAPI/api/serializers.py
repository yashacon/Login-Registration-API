from rest_framework import serializers
from .models import accounts,bio

class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model=accounts
        fields="__all__"
class bioSerializer(serializers.ModelSerializer):
    class Meta:
        model=bio
        fields="__all__"