from django.urls import path
from . import views


# Harus diberi ini agar hyperlink bisa diberi namespace
app_name = 'artikel'

urlpatterns = [
    path('', views.index, name='index'),
]
