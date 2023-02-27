from django.db import models
from django.utils.text import slugify

# Create your models here.
class Berita(models.Model):
    """
    Bagian dari halaman Artikel. Konten yang disajikan berupa berita seputar
    anime, manga, novel, musik dan budaya pop Jepang lainnya.
    """
    judul_berita = models.CharField(max_length=255)
    isi_berita = models.TextField()
    penulis = models.CharField(max_length=20, default="authors")
    kategori = models.CharField(max_length=20)
    waktu_post = models.DateTimeField(auto_now_add=True, editable=False)
    waktu_edit = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(max_length=255, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul_berita)
        super(Berita, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.judul_berita}"
