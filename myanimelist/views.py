from django.shortcuts import render


def index(request):
    context = {
        "page" : "Home",
        "website" : "Anime Indonesia",
    }
    return render(request, "index.html", context)
