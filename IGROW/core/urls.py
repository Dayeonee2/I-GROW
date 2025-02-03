from .views import university, reorganization, curriculum, survey
from django.urls import path, include

app_name = "core"

urlpatterns = [
    path("university/", university , name="university"),
    path("reorganization/", reorganization , name="reorganization"),
    path("curriculum/", curriculum , name="curriculum"),
    path("survey/", survey , name="survey"),
]
