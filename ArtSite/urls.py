"""
    ArtSite URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
    By doing so, this routes to all of the different apps within the project.

    Login, logout, and register route the the Users app (NOTE: login and logout use built in django views).
    "" routes to the Store app (by leaving this an empty string it becomes the 'home page' of the project)
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Store.urls")),
    path("register/", user_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="Users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="Users/logout.html"), name="logout")
]
