from django.db import models
from artists.models import Artist
from genres.models import Genre


class Album(models.Model):
    title = models.CharField(max_length=50)
    launch_date = models.DateField()
    artists = models.ManyToManyField(Artist, related_name='albums')
    genres = models.ManyToManyField(Genre, related_name='albums')

    def __str__(self):
        return self.title
