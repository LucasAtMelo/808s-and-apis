from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('CAN', 'Canada'),
    ('ENG', 'England'),)


class Artist(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=20, choices=NATIONALITY_CHOICES, default='USA')

    def __str__(self):
        return self.name
