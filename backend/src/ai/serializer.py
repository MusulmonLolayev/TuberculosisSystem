from rest_framework import serializers

from .models import Range

class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Range
        fields = '__all__'