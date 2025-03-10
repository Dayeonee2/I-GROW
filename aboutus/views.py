from django.shortcuts import render

# Create your views here.

def introduce(request):
    return render(request, 'aboutus/introduce.html')

def business(request):
    return render(request, 'aboutus/business.html')

def certified(request):
    return render(request, 'aboutus/certified.html')

def organization(request):
    return render(request, 'aboutus/organization.html')

def direction(request):
    return render(request, 'aboutus/direction.html')