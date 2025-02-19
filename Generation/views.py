from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {
    })

def profile(request):
    return render(request, 'profile.html', {
    })

def register(request):
    return render(request, 'register.html', {
    })

def authorization(request):
    return render(request, 'authorization.html', {
    })

