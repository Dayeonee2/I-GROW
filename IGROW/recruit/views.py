from django.shortcuts import render

# Create your views here.
def culture(request):
    return render(request, 'recruit/culture.html')

def recruit(request):
    return render(request, 'recruit/recruit.html')

def salary(request):
    return render(request, 'recruit/salary.html')