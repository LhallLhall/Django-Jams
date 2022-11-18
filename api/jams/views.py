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
    # http_method_names = ['get', 'post', 'put', 'delete']
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().create(request, *args, **kwargs)
    
    # def destroy(request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return super().destroy(request, *args, **kwargs)

class GenreAPIView(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
                raise Http404
        

    def get(self,request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = GenreSerializer(data)
        else:
            data = Genre.objects.all()
            serializer = GenreSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = GenreSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Genre Created Successfully',
            'data': serializer.data,
        }
        return response

    def put(self, request, pk=None, format=None):
        genre_to_update = Genre.objects.get(pk=pk)
        data = request.data
        serializer = GenreSerializer(instance=genre_to_update, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = {
            'message': 'Song Updated Successfully',
            'data': serializer.data
        }
        return response

class SongAPIView(APIView):
    def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
                raise Http404
        

    def get(self,request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = SongSerializer(data)
        else:
            data = Song.objects.all()
            serializer = SongSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = SongSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Song Created Successfully',
            'data': serializer.data,
        }
        return response

    def put(self, request, pk=None, format=None):
        pass