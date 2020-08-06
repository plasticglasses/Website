from django.shortcuts import render

# Create your views here.

def title_card_view(request, *args, **kwargs):
    return render(request, 'camping.webp', {})

def project_view(request, *args, **kwargs):
    return render(request, 'welcome.html', {})