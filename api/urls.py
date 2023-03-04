from django.urls import path
from . import views


app_name = 'api'

urlpatterns = [
    path('', views.getRoutes, name='index'),
    path('anime/', views.getAnime),
]
