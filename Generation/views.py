from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
import random
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from markdown_deux import markdown
from django.utils.safestring import mark_safe
from bleach import clean
from django.views.decorators.http import require_POST

def index(request):
    if not request.user.is_authenticated:
        posts = Post.objects.all()
    else:
        posts = Post.objects.order_by('-timestamp').exclude(user=request.user)
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

def create_post(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        allowed_tags = ['b', 'i', 'u', 'em', 'strong', 's']  # Разрешенные теги
        content = clean(content, tags=allowed_tags, strip=True)  # Очистка текста от запрещенных тегов
        content = mark_safe(markdown(content))  # Преобразование текста в markdown
        
        if content == '':
            messages.error(request, 'Пост не может быть пустым.')
            return redirect('profile', username=request.user.username)

        Post.objects.create(user=request.user, content=content)
        return redirect('profile', username=request.user.username)
    return redirect('profile', username=request.user.username)

@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    messages.success(request, 'Пост успешно удалён.')
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
            messages.error(request, 'Пароли не совпадают.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Имя пользователя уже занято.')
            return redirect('register')

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('index')

    return render(request, 'registration.html')


def authorization(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    else:
        messages.get_messages(request).used = True  # Удаляем старые сообщения
    return render(request, 'authorization.html')

def logout_user(request):
    logout(request)
    return index(request)