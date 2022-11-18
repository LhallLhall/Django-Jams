from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'song', SongViewSet)
router.register(r'artist', ArtistViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'playlist', PlaylistViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'artist_songs', ArtistWithSongsViewSet)
router.register(r'album_songs', AlbumWithSongsViewSet)
router.register(r'playlist_songs', PlaylistWithSongsViewSet)



urlpatterns = [
    # path('api/', SongAPIView.as_view()),
    # path('api/genre/', GenreAPIView.as_view()),
    # path('api/genre/<str:pk>/', GenreAPIView.as_view()),
    path('', include(router.urls))
]