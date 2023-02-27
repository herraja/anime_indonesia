from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "page" : "Artikel",
        "website" : "Anime Indonesia",
    }
    return render(request, "index.html", context)
