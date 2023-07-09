from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from apps.users.models import UserRegister

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import UserRegister

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password and username and email:
            try:
                user = UserRegister.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                authenticated_user = authenticate(request, username=username, password=password)
                if authenticated_user:
                    login(request, authenticated_user)
                    return redirect('index')
                else:
                    return redirect('index')
            except:
                return redirect('index')
        else:
            return redirect('index')
    return render(request, "register")

def login(requests):
    return render(requests, "login.html")
