from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Congratulations, You have created school_admin application using Django")


def loginfun(request):
    return render(request,'admin_templates/login.html')

