import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "Hero" : "Portal Komunitas Anime",
        "Lead" : "Terupdate se-Indonesia",
        "page" : "Daftar Anime",
        "website" : "Anime Indonesia",
    }
    return render(request, "animelist/index.html", context)

def search(request):
    search_query = requests.GET.get("q", "")
    response = requests.get(f"https://api.jikan.moe/v3/search/anime?q={search_query}")
    results = response.json()["results"]
    context = {
        "Hero" : "Portal Komunitas Anime",
        "Lead" : "Terupdate se-Indonesia",
        "page" : "Daftar Anime",
        "results" : results,
        "search_query" : search_query,
        "website" : "Anime Indonesia",
    }
    return render(request, "animelist/search_result.html", context)
