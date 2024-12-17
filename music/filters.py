import django_filters
from .models import Music
from performer.models import Artist, Band

class MusicFilter(django_filters.FilterSet):
    performer = django_filters.CharFilter(method='filter_by_performer', label='Performer')

    class Meta:
        model = Music
        fields = ['genre', 'performer']

    def filter_by_performer(self, queryset, name, value):
        # Filtrer par artiste
        artist_queryset = Artist.objects.filter(name__icontains=value)
        # Filtrer par groupe
        band_queryset = Band.objects.filter(name__icontains=value)

        if artist_queryset.exists():
            queryset = queryset.filter(artists__in=artist_queryset)
        elif band_queryset.exists():
            queryset = queryset.filter(band__in=band_queryset)
        return queryset
