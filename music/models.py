from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=256)
    album_title = models.CharField(max_length=512)
    genre = models.CharField(max_length=128)
    album_logo = models.ImageField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=16)
    song_title = models.CharField(max_length=256)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
