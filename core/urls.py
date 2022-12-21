from django.urls import path
from . import views


urlpatterns = [
    path("home_page/", views.home_page),
    path("result_page/", views.result_page),
]