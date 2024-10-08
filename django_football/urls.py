"""
URL configuration for django_football project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mercato import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('show_team/<int:id>/',views.show_team, name="showTeam"),
    path('back/',views.back,name='back'),
    path('back/new_team/',views.store_team,name="newTeam"),
    path('back/update_team/<int:id>/',views.update_team,name='update_team'),
    path('back/delete_team/<int:id>/',views.delete_team,name='delete_team'),
    path('back/create_player/', views.create_player, name='create_player'),
    path('back/update_player/<int:id>/', views.update_player, name='update_player'),
    path('back/delete_player/<int:id>/', views.delete_player, name='delete_player'),
    path('players/', views.players, name='players'),
    path('show_player/<int:id>/', views.show_player, name='show_player'),
    ]



