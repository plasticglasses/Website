from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def project_view(request, *args, **kwargs):
    return render(request, 'welcome.html', {})
