from django.urls import path
from apps.auth.views import UserCreate

app_name = 'auth'

urlpatterns = [
    path('register/', UserCreate.as_view(), name='create_user'),
]