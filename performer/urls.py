from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, BandViewSet

router = DefaultRouter()
router.register(r'artists', ArtistViewSet)
router.register(r'bands', BandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]