from django.contrib import admin
from artists.models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_date', 'nationality')
