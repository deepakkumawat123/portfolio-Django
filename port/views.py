from django.shortcuts import render
from . models import *
# Create your views here.

def index(request):
    about=About.objects.first()
    skill=Skills.objects.all()
    education=Education.objects.all()
    experience=Experience.objects.all()
    portfoli=portfolio.objects.all()
    service=Service.objects.all()
    return render(request,'index.html',{'about':about, 'skill':skill,'education':education,'experience':experience,'portfolio':portfolio,'service':service})
