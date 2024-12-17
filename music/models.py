from django.db import models
from performer.models import Band, Artist
from django.urls import reverse

class Album(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

    def get_absolute_url(self):
        return reverse('music:album-detail', kwargs={'pk': self.pk})

class Music(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.SET_NULL, null=True, blank=True)
    artists = models.ManyToManyField(Artist, through='MusicArtist', related_name='tracks')

class MusicArtist(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
