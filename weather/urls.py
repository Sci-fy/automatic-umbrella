# weather/urls.py
from django.urls import path
from .views import home, register, history

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('history/', history, name='history'),
]

