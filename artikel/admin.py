from django.contrib import admin
from .models import Berita

# Register your models here.
class AdminBerita(admin.ModelAdmin):
    readonly_fields = ['waktu_post' 'waktu_edit', 'slug']

admin.site.register(Berita)
