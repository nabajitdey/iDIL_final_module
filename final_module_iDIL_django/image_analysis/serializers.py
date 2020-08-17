from rest_framework import serializers
from .models import Object

class ObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'