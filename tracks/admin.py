from django.contrib import admin
from tracks.models import Track, TrackArtist


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):

    list_display = ['title', 'album', 'track_number', 'duration_seconds', 'is_explicit']


@admin.register(TrackArtist)
class TrackArtistAdmin(admin.ModelAdmin):

    list_display = ['role', ]
