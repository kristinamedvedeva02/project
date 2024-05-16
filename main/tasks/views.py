from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser

class OfficeTaskViewSet(viewsets.ModelViewSet):
    queryset = OfficeTask.objects.all()
    serializer_class = OfficeTaskSerializer
    permission_classes = [IsAdminUser]


class TeamTaskViewSet(viewsets.ModelViewSet):
    queryset = TeamTask.objects.all()
    serializer_class = TeamTaskSerializer
    permission_classes = [IsAdminUser]



class PersonalTaskViewSet(viewsets.ModelViewSet):
    queryset = PersonalTask.objects.all()
    serializer_class = PersonalTaskSerializer
    permission_classes = [IsAdminUser]