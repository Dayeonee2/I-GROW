from .views import aboutus
from django.urls import path, include

app_name = "aboutus"

urlpatterns = [
    path("", aboutus)
]