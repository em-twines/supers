from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter ego', 'primary ability', 'secondary ability', 'catchphrase', 'super type', 'super type id']
