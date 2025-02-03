from .views import idealcandidate, benefits, salary
from django.urls import path, include

app_name = "recuit"

urlpatterns = [
    path("idealcandidate", idealcandidate, name="idealcandidate"),
    path("benefits", benefits, name="benefits"),
    path("salary", salary, name="salary"),
]