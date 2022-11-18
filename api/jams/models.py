from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200, null=False)
    album = models.ManyToManyField('Album', related_name='album_songs')
    duration = models.FloatField(null=False)
    artist = models.ManyToManyField('Artist', related_name='artists_songs')
    playlist = models.ManyToManyField('Playlist', related_name='playlists_songs')
    genre = models.ForeignKey('Genre', related_name='genres', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.name