from django.shortcuts import render

# Create your views here.
def recuit(request):
    return render(request, 'recuit/idealcandidate.html')