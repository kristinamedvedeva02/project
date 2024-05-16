from rest_framework import routers
from .views import *
from django.urls import path, include

routers = routers.SimpleRouter()
routers.register(r'companies', CompanyViewSet)
routers.register(r'offices', OfficeViewSet)



urlpatterns = [
    path('', include(routers.urls))
]
