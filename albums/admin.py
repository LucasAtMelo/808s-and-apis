from django.contrib import admin
from albums.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):

    list_display = ['id', 'title', 'launch_date']
