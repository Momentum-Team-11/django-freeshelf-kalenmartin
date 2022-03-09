from operator import truediv
from django.db import models
from django.contrib.auth.models import AbstractUser
from multiprocessing import AuthenticationError


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

    def __str__(self):
        return self.title