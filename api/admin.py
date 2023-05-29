from django.contrib import admin
from .models import Anime


# Register your models here.
class AnimeAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "updated", "created"]


admin.site.register(Anime, admin_class=AnimeAdmin)