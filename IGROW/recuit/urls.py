from .views import recuit
from django.urls import path, include

app_name = "recuit"

urlpatterns = [
    path("", recuit)
]