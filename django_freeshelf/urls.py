"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from books import views as books_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', books_views.index, name="index"),
    path('books/<int:pk>/', books_views.details, name="details"),
    path('books/add/', books_views.add, name='add'),
    path('books/<int:pk>/edit/', books_views.edit, name='edit'),
    path('books/<int:pk>/delete/', books_views.delete, name='delete'),
    # path('', books_views.login, name='login'),
    path('auth/', include('registration.backends.simple.urls')),
    path('books/<int:pk>/favorite/', books_views.favorite, name='favorite'),
    # path('books/categories/<slug:slug>', books_views.categories, name="categories"),
]