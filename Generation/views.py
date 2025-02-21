from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
import random
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html', {
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
    return render(request, 'register.html', {
    })

def authorization(request):
    return render(request, 'authorization.html', {
    })

