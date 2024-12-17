from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusicViewSet, AlbumViewSet, MusicArtistViewSet

router = DefaultRouter()
router.register(r'music', MusicViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'music-artists', MusicArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]