from rest_framework import serializers
from .models import *

class MathHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MathHistory
        fields = '__all__'