from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
import random
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.exclude(user=request.user)
    posts = random.sample(list(posts), min(20, len(posts)))
    return render(request, 'index.html', {
        'posts': posts,
    })

def profile(request, username):
    
    profile_user = get_object_or_404(User, username=username)
    # Получаем все посты пользователя (при желании можно сортировать)
    posts = Post.objects.filter(user=profile_user).order_by('-timestamp')

    context = {
        'profile_user': profile_user,
        'posts': posts,
    }
    return render(request, 'profile.html', context)

# @login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        Post.objects.create(user=request.user, content=content)
        return redirect('profile', username=request.user.username)
    return redirect('profile', username=request.user.username)

def register(request):
    return render(request, 'registration.html', {
    })


def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        if password1 != password2:
            return render(request, 'registration.html', {
                'error': 'Passwords do not match.'
            })
        
        if User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {
                'error': 'Username already exists.'
            })
        
        # Continue with user creation if validations pass
        user = User.objects.create_user(username=username, password=password1)
        user.save()
        login(request, user)

        return render(request, 'index.html', {})


def authorization(request):
    return render(request, 'authorization.html', {
    })

def logout_user(request):
    logout(request)
    return render(request, 'index.html', {
    })