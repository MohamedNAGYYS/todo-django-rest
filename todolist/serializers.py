from rest_framework import serializers
from .models import ToDo

class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty!")
        return value