from django.urls import path
from . import views
from .views import JobListAPI,JobCreateAPI,UserTestAPI

urlpatterns = [
    # path("", views.home, name="home"),
    path("api/jobs/", JobListAPI.as_view()),
    path("api/jobs/create/", JobCreateAPI.as_view()),
    path("api/user-test/", UserTestAPI.as_view()),
]

