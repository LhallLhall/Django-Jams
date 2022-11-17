from django.urls import path, include
from .views import SongViewSet, ArtistViewSet, GenreViewSet, PlaylistViewSet, AlbumViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'song', SongViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'playlist', PlaylistViewSet)
router.register(r'album', AlbumViewSet)



urlpatterns = [
    
    path('', include(router.urls))
]