from rest_framework import serializers
from .models import SecurityFeature

class SecurityFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityFeature
        fields = '__all__'
