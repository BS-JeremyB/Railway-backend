from django.urls import path
from .views import UserResgisterView


urlpatterns = [
    path('auth/register/', UserResgisterView.as_view(), name='user_register')
]
