from django.shortcuts import render


def index(request):
    context = {
        "page" : "Beranda",
        "website" : "Anime Indonesia",
    }
    return render(request, "index.html", context)
