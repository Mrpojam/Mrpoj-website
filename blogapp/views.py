from django.shortcuts import render
#from django.http import HttpResponse
from .models import Settings, Experince, Education, Skills, Tools, Awards
def index (request):
    context = {
        'settings' : Settings.objects.get(id=1),
        'experinces' : Experince.objects.all(),
        'education' : Education.objects.all(),
        'skills' : Skills.objects.all(),
        'tools' : Tools.objects.all(),
        'awards' : Awards.objects.all(),
    }
    return render (request, 'blogapp/index.html', context)
