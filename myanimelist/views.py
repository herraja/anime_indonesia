from api.models import Anime as ApiAnime
from django.shortcuts import render


def index(request):
    anime = ApiAnime.objects.all()
    context = {
        "Anime" : anime.order_by("anime_title"),
        "Hero" : "Portal Komunitas Anime",
        "Lead" : "Terupdate se-Indonesia",
        "page" : "Beranda",
        "website" : "Anime Indonesia",
    }
    return render(request, "index.html", context)
