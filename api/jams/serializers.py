from rest_framework import serializers
from .models import *
from .fields import NameListingField

class AlbumSerializer(serializers.ModelSerializer):
    songs = NameListingField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['album_title', 'songs']

class ArtistSerializer(serializers.ModelSerializer):
    artists_songs = NameListingField(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('artist_name', 'artists_songs')

class PlaylistSerializer(serializers.ModelSerializer):
    playlists_songs = NameListingField(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = ['playlist_title', 'playlists_songs']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['id']

class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(many=True)
    artist = ArtistSerializer(many=True)
    playlist = PlaylistSerializer(many=True)
    genre = GenreSerializer(many=False)
    class Meta:
        model = Song
        fields = (
            'title',
            'artist',
            'duration',
            'album',
            'playlist',
            'genre'
        )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    # def delete():
    #     pass

