from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Song
from django.forms.models import model_to_dict
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import generics
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *

# Create your views here.
class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    http_method_names = ['get', 'post', 'put', 'delete']