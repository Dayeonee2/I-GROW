from django.shortcuts import render
from django.conf import settings  # settings.py 불러오기

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
    context = {
        'NAVER_CLIENT_ID': settings.NAVER_CLIENT_ID  # 네이버 지도 API 키 전달
    }
    return render(request, 'aboutus/direction.html', context)