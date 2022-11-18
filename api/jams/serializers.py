from rest_framework import serializers
from .models import *
from .fields import NameListingField, GenreField, ArtistField, PlaylistField, AlbumField

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
class AlbumWithSongsSerializer(serializers.ModelSerializer):
    album_songs = NameListingField(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ['id','title', 'album_songs']
        # 'songs'
class ArtistWithSongsSerializer(serializers.ModelSerializer):
    artists_songs = NameListingField(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ['id','name', 'artists_songs']
class PlaylistWithSongsSerializer(serializers.ModelSerializer):
    playlists_songs = NameListingField(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = ['id','title', 'playlists_songs']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        # 'artists_songs'

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
        # 'playlists_songs'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ['id']

class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(many=True)
    # artist = ArtistSerializer(many=True)
    # playlist = PlaylistSerializer(many=True)
    # genre = GenreSerializer(many=False)
    album = AlbumField(many=True, queryset=Album.objects.all())
    playlist = PlaylistField(many=True, queryset=Playlist.objects.all())
    genre = GenreField(queryset=Genre.objects.all())
    artist = ArtistField(many=True, queryset=Artist.objects.all())
    class Meta:
        model = Song
        fields = (
            'id',
            'title',
            'artist',
            'duration',
            'album',
            'playlist',
            'genre'
        )

    # def create(self, validated_data):
    #     pass

    # def update(self, instance, validated_data):
    #     pass

    # def delete():
    #     pass

