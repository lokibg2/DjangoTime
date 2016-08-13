from django.db import models

# Create your models here.


class Album(models.Model):
    albumTitle = models.CharField(max_length=250)
    artist = models.CharField(max_length=500)
    genre = models.CharField(max_length=50)
    albumArt = models.CharField(max_length=500)

    def __str__(self):
        return self.albumTitle + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    songTitle = models.CharField(max_length=300)
    fileType = models.CharField(max_length=10)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.songTitle