# weather/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .utils import get_weather
from .models import WeatherQuery

def home(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather(city)
        if request.user.is_authenticated:
            WeatherQuery.objects.create(user=request.user, location=city)
    return render(request, 'weather/home.html', {'weather_data': weather_data})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'weather/register.html', {'form': form})

def history(request):
    if request.user.is_authenticated:
        queries = WeatherQuery.objects.filter(user=request.user)
    else:
        queries = []
    return render(request, 'weather/history.html', {'queries': queries})

