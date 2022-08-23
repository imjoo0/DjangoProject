"""DjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from articles import views

app_name = 'articles'
urlpatterns = [
    path('index/',views.index),
    path('dinner/',views.dinner,name='dinner'),
    path("review/", views.review),
    path("create_review/", views.create_review,name='create_review'),
    path("<int:pk>/",views.detail,name='detail'),
    path("<int:pk>/delete/",views.detail,name='delete'),
    path("<int:pk>/edit/",views.edit,name='edit'),
    path("<int:pk>/update/",views.update,name='update'),
]
