from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'myanimelist'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('artikel/', include('artikel.urls', namespace="artikel")),
]
