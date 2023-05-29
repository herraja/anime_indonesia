from django.db import models
from django.utils.text import slugify


# Create your models here.
class Anime(models.Model):
    mal_id = models.IntegerField(unique=True)
    anime_title = models.CharField(max_length=255)
    anime_score = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    airing_time = models.CharField(max_length=50, blank=True)
    studio = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=255, editable=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    api_url = models.CharField(blank=True, max_length=255)  # Jikan.moe API
    post_url = models.CharField(blank=True, max_length=255)  # Untuk akses poster dari API Jikan

    def save(self, *args, **kwargs):
        self.slug = slugify(self.anime_title)
        super(Anime, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.id}. {self.anime_title}"
    
    class Meta:
        ordering = ["-anime_score"]
