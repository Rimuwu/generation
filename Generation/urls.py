"""
URL configuration for Generation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('authorization/', views.authorization, name='authorization'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_user/', views.create_user, name='create_user'),
    path('logout/', views.logout_user, name='logout'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
