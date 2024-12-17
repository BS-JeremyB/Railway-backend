from django.db import models

class Performer(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)

    class Meta:
        abstract = True

class Artist(Performer):
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField()

class Band(Performer):
    formation_year = models.IntegerField()
