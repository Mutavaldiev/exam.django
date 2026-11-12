from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Books, Orders


def home(request):
    return render(request, 'home.html')




def books(request):
    data = Books.objects.all()
    return render(request, 'books.html', {'books': data})





def add_books(request):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        Books.objects.create(
            name=request.POST.get('name'),
            title=request.POST.get('title'),
            caption=request.POST.get('caption'),
            due_date=request.POST.get('due_date'),
            picture=request.FILES.get('picture'),
            quantity=quantity,available=quantity,)
        return redirect('books')
    return render(request, 'book_form.html')





def update_book(request, id):
    book = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))
        book.available = book.available + new_quantity - book.quantity
        book.quantity = new_quantity
        book.name = request.POST.get('name')
        book.title = request.POST.get('title')
        book.caption = request.POST.get('caption')
        book.due_date = request.POST.get('due_date')
        book.picture = request.FILES.get('picture', book.picture)
        return redirect('books')
    return render(request, 'book_form.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Books, id=id)
    if request.method == 'POST':
        book.delete()
    return redirect('books')




def authors(request):
    data = Author.objects.all()
    return render(request, 'authors.html', {'authors': data})




def create_author(request):
    if request.method == 'POST':
        Author.objects.create(
            name_author=request.POST.get('name_author'),
            book=request.POST.get('book'),
            is_active=request.POST.get('is_active') == 'True')
        return redirect('authors')
    return render(request, 'author_form.html')




def update_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.name_author = request.POST.get('name_author')
        author.book = request.POST.get('book')
        author.is_active = request.POST.get('is_active') == 'True'
        return redirect('authors')
    return render(request, 'author_form.html', {'author': author})




def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.delete()
    return redirect('authors')




def orders(request):
    if request.method == 'POST':
        book = get_object_or_404(Books, id=request.POST.get('books_id'))
        quantity = int(request.POST.get('quantity'))
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        days = (datetime.strptime(end_date, '%Y-%m-%d') - datetime.strptime(start_date, '%Y-%m-%d')).days
        book.available = book.available - quantity
        return redirect('orders')
    return render(request, 'orders.html', {'books': Books.objects.all(), 'orders': Orders.objects.all(), })





def delete_order(request, id):
    order = get_object_or_404(Orders, id=id)
    if request.method == 'POST':
        order.books_id.available = order.books_id.available + order.quantity
        order.books_id.save()
        order.delete()
    return redirect('orders')