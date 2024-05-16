from rest_framework import serializers
from .models import *

class OfficeTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = OfficeTask
        read_only_fields = ()


class TeamTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = TeamTask
        read_only_fields = ()


class PersonalTaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = PersonalTask
        read_only_fields = ()
