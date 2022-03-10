from unicodedata import category
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, User
from .forms import BookForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, "login.html")


@login_required(login_url="auth_login")
def index(request):
    books =  Book.objects.order_by('-created_at')

    return render(request, "index.html",
        {"books": books})


def details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()

    return render(request, "details.html",
        {"book": book, "form": form, "pk": pk})


@login_required(login_url="auth_login")
def add(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user_id = pk
            form.save()
            return redirect(to='index')

    return render(request, "add.html",
        {"form": form, "user": user})


@login_required(login_url="auth_login")
def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='index')

    return render(request, "edit.html",
        {"form": form, "book": book})


@login_required(login_url="auth_login")
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='index')

    return render(request, "delete.html",
        {"book": book})


def favorite(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        favorite = Book
    else:
        favorite = Book(request.method == 'POST')
        Book.objects.filter(pk=book.pk).update(favorite="✔️")
        return redirect(to='favorite')
    return render(request, "index.html",
        {"book": book, "favorite": favorite})


@login_required
def add_favorite(request, books_pk):
    books = get_object_or_404(Book, pk=books_pk)
    user = request.user
    user.favorite_books.add(books)
    return redirect(to="index")


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.filter(category__slug=slug)

    return render(request, "categories.html",
        {"books": books, "category": category})