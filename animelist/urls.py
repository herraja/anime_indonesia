from django.urls import path
from . import views


app_name = "animelist"

urlpatterns = [
    path('', views.index, name="index"),
]
