from rest_framework import serializers
from .models import Music, Album, MusicArtist
from performer.models import Artist, Band

class MusicArtistSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(view_name='performer:artist-detail', queryset=Artist.objects.all())  # Vous pouvez aussi utiliser ArtistSerializer si vous avez besoin de plus de détails

    class Meta:
        model = MusicArtist
        fields = ['url', 'artist', 'role']
        extra_kwargs = {
            'url': {'view_name': 'music:musicartist-detail'}
        }

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(view_name='music:music-detail', many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['url', 'name', 'year', 'tracks']
        extra_kwargs = {
            'url': {'view_name': 'music:album-detail'}
        }

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.HyperlinkedRelatedField(view_name='music:album-detail', queryset=Album.objects.all(), required=False, allow_null=True)
    band = serializers.HyperlinkedRelatedField(view_name='performer:band-detail', queryset=Band.objects.all(), required=False, allow_null=True)
    artists = MusicArtistSerializer(many=True, source='musicartist_set')  # Ajoutez `source` pour la relation ManyToMany via MusicArtist

    class Meta:
        model = Music
        fields = ['url', 'name', 'year', 'genre', 'band', 'album', 'artists']
        extra_kwargs = {
            'url': {'view_name': 'music:music-detail'}
        }

    def create(self, validated_data):
        # Utiliser la clé correcte pour extraire les données des artistes
        artists_data = validated_data.pop('musicartist_set', [])
        album_data = validated_data.pop('album', None)
        band_data = validated_data.pop('band', None)

        # Créer l'objet Music
        music = Music.objects.create(**validated_data)

        # Associer les artistes au morceau de musique
        for artist_data in artists_data:
            artist = artist_data.pop('artist')
            MusicArtist.objects.create(music=music, artist=artist, **artist_data)

        # Assigner l'album si présent
        if album_data:
            music.album = album_data
            music.save()

        # Assigner le groupe si présent
        if band_data:
            music.band = band_data
            music.save()

        return music

    def update(self, instance, validated_data):
        # Utiliser la clé correcte pour extraire les données des artistes
        artists_data = validated_data.pop('musicartist_set', [])
        album_data = validated_data.pop('album', None)
        band_data = validated_data.pop('band', None)

        # Mettre à jour les autres champs de l'objet Music
        instance = super().update(instance, validated_data)

        # Supprimer les artistes existants et ajouter les nouveaux
        instance.musicartist_set.all().delete()
        for artist_data in artists_data:
            artist = artist_data.pop('artist')
            MusicArtist.objects.create(music=instance, artist=artist, **artist_data)

        # Mettre à jour l'album si présent
        if album_data:
            instance.album = album_data
            instance.save()

        # Mettre à jour le groupe si présent
        if band_data:
            instance.band = band_data
            instance.save()

        return instance
