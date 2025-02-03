from django.urls import path
from .views import introduce, business, certified, organization, direction  # 필요한 뷰 함수들 추가

app_name = "aboutus"

urlpatterns = [
    path("introduce/", introduce, name="introduce"),
    path("business/", business, name="business"),
    path("certified/", certified, name="certified"),
    path("organization/", organization, name="organization"),
    path("direction/", direction, name="direction"),
]
