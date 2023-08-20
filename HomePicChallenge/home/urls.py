from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.home , name="home_view"),
    path("under_work/", views.under_work, name="working"),
    
]