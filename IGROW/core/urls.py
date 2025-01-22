from .views import core
from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("", core)
]