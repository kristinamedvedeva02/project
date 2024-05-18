from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.renderers import *
from .forms import *
from django.http import HttpResponseRedirect
from users.models import *


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    model = Company


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.filter(company = request.user.company)
    serializer_class = OfficeSerializer
    model = Office



class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    model = Team


class AddOfficeAPIView(APIView):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
    template_name = 'company_structure/add_office.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        form = OfficeCreationForm(request.POST)
        
        if form.is_valid():
            new_office = form.save(commit= False)
            company = form.cleaned_data['company']
            name = form.cleaned_data['name']

            new_office.save()
            return HttpResponseRedirect("/New office has been added/")

    # if a GET (or any other method) we'll create a blank form
        # else:
        #     form = OfficeCreationForm()

        # return render(request, "company_structure/add_office.html", {"form": form})
