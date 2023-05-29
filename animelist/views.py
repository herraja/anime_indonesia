import requests
from django.shortcuts import render
from api.models import Anime as ApiAnime

# Create your views here.
def index(request):
    anime = ApiAnime.objects.all()
    context = {
        "Anime" : anime,
        "Hero" : "Portal Komunitas Anime",
        "Lead" : "Terupdate se-Indonesia",
        "page" : "Daftar Anime",
        "website" : "Anime Indonesia",
    }
    return render(request, "animelist/index.html", context)

