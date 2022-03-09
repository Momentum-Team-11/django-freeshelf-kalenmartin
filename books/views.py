from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.

def index(request):
    books =  Book.objects.all()

    return render(request, "index.html",
        {"books": books})


def details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm()

    return render(request, "details.html",
        {"book": book, "form": form, "pk": pk})


def add(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='index')

    return render(request, "add.html",
        {"form": form})


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


def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='index')

    return render(request, "delete.html",
        {"book": book})