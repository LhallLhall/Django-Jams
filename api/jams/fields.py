from rest_framework import serializers
from .models import *

class NameListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.title

class AlbumField(serializers.RelatedField):
    def to_internal_value(self, data):
        album_obj, created = Album.objects.get_or_create(**data)
        return album_obj
    def to_representation(self, value):
        return {
            "title": value.title
        }
class GenreField(serializers.RelatedField):
    def to_internal_value(self, data):
        genre_obj, created = Genre.objects.get_or_create(**data)
        return genre_obj
    def to_representation(self, value):
        return {
            "title": value.title
        }
class ArtistField(serializers.RelatedField):
    def to_internal_value(self, data):
        artist_obj, created = Artist.objects.get_or_create(**data)
        return artist_obj
    def to_representation(self, value):
        return {
            "name": value.name
        }

class PlaylistField(serializers.RelatedField):
    def to_internal_value(self, data):
        playlist_obj, created = Playlist.objects.get_or_create(**data)
        return playlist_obj
    def to_representation(self, value):
        return {
            "title": value.title
        }