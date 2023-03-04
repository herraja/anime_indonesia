from django.shortcuts import render


def index(request):
    context = {
        "Hero" : "Portal Komunitas Anime",
        "Lead" : "Terupdate se-Indonesia",
        "page" : "Beranda",
        "website" : "Anime Indonesia",
    }
    return render(request, "index.html", context)
