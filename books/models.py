from django.db import models
from django.contrib.auth.models import AbstractUser
from multiprocessing import AuthenticationError
from django.utils.text import slugify


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    URL = models.URLField(max_length=300, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorite = models.CharField(max_length=1, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="books")

    # favorited_by = models.ManyToManyField("user", related_name="favorite_books")

    def __str__(self):
        return self.title