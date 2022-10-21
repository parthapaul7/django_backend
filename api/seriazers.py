from rest_framework import serializers
from .models import Country 

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
    def to_representation(self, instance):
        return super().to_representation(instance)