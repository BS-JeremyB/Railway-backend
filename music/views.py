from rest_framework import viewsets
from .models import Music, Album, MusicArtist
from .serializers import MusicSerializer, AlbumSerializer, MusicArtistSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MusicFilter

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MusicFilter  # Utiliser le filtre personnalisé

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class MusicArtistViewSet(viewsets.ModelViewSet):
    queryset = MusicArtist.objects.all()
    serializer_class = MusicArtistSerializer