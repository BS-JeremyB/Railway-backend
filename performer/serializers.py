from rest_framework import serializers
from .models import Artist, Band
from music.models import Music, Album

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True, 
        view_name='music:music-detail', 
        read_only=True
    )
    albums = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ['url', 'first_name', 'name', 'genre', 'origin', 'birth_date', 'tracks', 'albums']
        extra_kwargs = {
            'url': {'view_name': 'performer:artist-detail'}
        }


    def get_albums(self, obj):
        # Obtenir une liste unique d'albums via les musiques de l'artiste
        albums = Album.objects.filter(tracks__artists=obj).distinct()
        request = self.context.get('request')
        return [self.context['request'].build_absolute_uri(album.get_absolute_url()) for album in albums]



class BandSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True, 
        view_name='music:music-detail', 
        read_only=True,
        source='music_set'
    )
    albums = serializers.SerializerMethodField()

    class Meta:
        model = Band
        fields = ['url', 'name', 'genre', 'origin', 'formation_year', 'tracks', 'albums']
        extra_kwargs = {
            'url': {'view_name': 'performer:band-detail'}
        }


    def get_albums(self, obj):
        # Obtenir une liste unique d'albums via les musiques du groupe
        albums = Album.objects.filter(tracks__band=obj).distinct()
        request = self.context.get('request')
        return [self.context['request'].build_absolute_uri(album.get_absolute_url()) for album in albums]