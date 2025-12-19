from django.db import models
from albums.models import Album
from artists.models import Artist


ROLE_CHOICES = (
    ('PROD', 'Produtor'),
    ('MAIN', 'Principal'),
    ('FEAT', 'Participação'),
    ('LYRC', 'Letrista'),

)


class Track(models.Model):
    title = models.CharField(max_length=60)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    track_number = models.IntegerField()
    duration_seconds = models.IntegerField()
    is_explicit = models.BooleanField(default=False)
    artists = models.ManyToManyField(Artist, through='TrackArtist', related_name='tracks')

    def __str__(self):
        return self.title


class TrackArtist(models.Model):
    artist = models.ForeignKey(Artist, related_name='artist_roles', on_delete=models.CASCADE)
    track = models.ForeignKey(Track, related_name='artist_roles', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='MAIN')

    def __str__(self):
        return f"{self.artist} - {self.track} ({self.role})"
