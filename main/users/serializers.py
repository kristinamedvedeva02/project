from rest_framework import serializers
from .models import *
from .permissions import *
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password], style={'input_type': 'password'})

    class Meta:
        fields = ['id', 'username', 'first_name', 'surname', 'middle_name', 'role', 'company', 'office', 'team', 'password']
        model = User
        read_only_fields = ('id', 'created', 'updated')
        write_only_fields = ('password',)


    # def save(self):
    #     user = self.context['request'].user    
    #     if user.role == Roles.COMPANY_ADMIN:
    #         company = self.context['request'].user.company
    #         return User.objects.create(company=company, **self.validated_data)