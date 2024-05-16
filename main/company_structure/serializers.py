from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Company
        read_only_fields = ('created', 'updated')


class OfficeSerializer(serializers.ModelSerializer):


    class Meta:
        fields = '__all__'
        model = Office
        read_only_fields = ('created', 'updated', 'company')

    def save(self, **kwargs):
        company = self.context['request'].user.company
        return Office.objects.create(company=company, **self.validated_data)


