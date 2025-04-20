from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def Home(request):
    return render(request, 'home.html')


def signup_parent(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('signup_parent')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken')
            return redirect('signup_parent')

        user = User.objects.create_user(username=username, email=email, password=password)
        Parent.objects.create(user=user, phone=phone)
        login(request, user)
        return redirect('home')

    return render(request, 'auth/signup_parent.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'auth/login.html')

