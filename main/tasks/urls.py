from rest_framework import routers
from .views import *
from django.urls import path, include

routers = routers.DefaultRouter()
routers.register(r'office_tasks', OfficeTaskViewSet)
routers.register(r'team_tasks', TeamTaskViewSet)
routers.register(r'personal_tasks', PersonalTaskViewSet)

urlpatterns = [
    path('', include(routers.urls))
]
