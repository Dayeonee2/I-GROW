from .views import culture, recruit, salary
from django.urls import path, include

app_name = "recruit"

urlpatterns = [
    path("culture", culture, name="culture"),
    path("recruit", recruit, name="recruit"),
    path("salary", salary, name="salary"),
]