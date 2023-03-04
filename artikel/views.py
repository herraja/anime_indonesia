from django.shortcuts import render
from .models import Berita

# Create your views here.
def index(request):
    """
    Function untuk menampilkan seluruh artikel berita di dalam database kami.
    Bentuk URL dari function ini -> http://localhost:8000/artikel/
    """
    berita = Berita.objects.all()
    context = {
        "Hero" : "Portal Komunitas Anime",
        "Lead" : "Terupdate se-Indonesia",
        "page" : "Artikel",
        "post_berita" : berita,
        "website" : "Anime Indonesia",
    }
    return render(request, "artikel/index.html", context)

def detail(request, category, inputSlug):
    """
    Function untuk membaca satu judul konten berita.
    Bentuk URL dari function ini adalah seperti dibawah ini
    1. http://localhost:8000/artikel/hot_news/penyanyi-anisong-maon-kurosaki-meninggal-dunia/
    2. http://localhost:8000/artikel/incoming_event/comic-frontier-16-siap-digelar-maret-2023/
    """
    berita = Berita.objects.get(kategori=category, slug=inputSlug)
    context = {
        "detail_berita": berita,
        "Hero" : "Portal Komunitas Anime",
        "Lead" : "Terupdate se-Indonesia",
        "page": "Artikel",
        "website": "Anime Indonesia",
    }
    return render(request, "artikel/detail.html", context)
