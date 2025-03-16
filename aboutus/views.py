from django.shortcuts import render
from django.conf import settings  # settings.py 불러오기
import requests

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
    address = "서울특별시 서초구 남부순환로350길 8, 용연빌딩 3층"  # 원하는 주소 설정
    geocode_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

    headers = {
        "X-NCP-APIGW-API-KEY-ID": settings.NAVER_CLIENT_ID,
        "X-NCP-APIGW-API-KEY": settings.NAVER_CLIENT_SECRET
    }
    params = {"query": address}

    response = requests.get(geocode_url, headers=headers, params=params)
    data = response.json()

    # 좌표 데이터 추출
    if "addresses" in data and data["addresses"]:
        latitude = data["addresses"][0]["y"]  # 위도
        longitude = data["addresses"][0]["x"]  # 경도
    else:
        latitude, longitude = None, None  # 오류 처리

    context = {
        "NAVER_CLIENT_ID": settings.NAVER_CLIENT_ID,
        "latitude": latitude,
        "longitude": longitude,
        "address": address,
        "api_response": data  # 프론트에서 확인 가능하도록 전달
    }
    return render(request, "aboutus/direction.html", context)