from rest_framework import serializers
from .models import *
from .permissions import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['first_name', 'surname', 'middle_name', 'role', 'company', 'office', 'team']
        model = User
        read_only_fields = ('created', 'updated')


    # def save(self):
    #     user = self.context['request'].user    
    #     if user.role == Roles.COMPANY_ADMIN:
    #         company = self.context['request'].user.company
    #         return User.objects.create(company=company, **self.validated_data)