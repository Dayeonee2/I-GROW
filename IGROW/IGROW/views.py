from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main.html')

def contact(request):
    return render(request, 'contact.html')