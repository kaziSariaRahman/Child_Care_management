from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def Home(request):
    return render(request, 'home.html')
