from django.shortcuts import render

# Create your views here.
def idealcandidate(request):
    return render(request, 'recuit/idealcandidate.html')

def benefits(request):
    return render(request, 'recuit/benefits.html')

def salary(request):
    return render(request, 'recuit/salary.html')