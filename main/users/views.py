from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'base.html'
    
    # def get_queryset(self):
    #     return User.objects.all()

    # def get(self, request):
    #     queryset = User.objects.all()
    #     return Response({'users': queryset})



class UserApiView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users/users.html'

    def get(self, request):
        queryset = User.objects.all()
        return Response({'users': queryset})
        


    



