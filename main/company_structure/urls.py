from rest_framework import routers
from .views import *
from django.urls import path, include, re_path

routers = routers.SimpleRouter()
routers.register(r'companies', CompanyViewSet)
routers.register(r'offices', OfficeViewSet)
routers.register(r'teams', TeamViewSet)



urlpatterns = [
    path('', include(routers.urls)),
    path('add_office', AddOfficeAPIView.as_view(), name='add_office'),

]
