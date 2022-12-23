from django.urls import path
from .views import home_page, result_page


urlpatterns = [
    path("", home_page),
    path("result_page/", result_page),
]