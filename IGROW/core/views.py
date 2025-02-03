from django.shortcuts import render

# Create your views here.
def university(request):
    return render(request, 'core/university.html')

def reorganization(request):
    return render(request, 'core/reorganization.html')

def curriculum(request):
    return render(request, 'core/curriculum.html')

def survey(request):
    return render(request, 'core/survey.html')