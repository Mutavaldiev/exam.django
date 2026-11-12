from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('add_books/', add_books, name='add_books'),
    path('books/<int:id>/update/', update_book, name='update_book'),
    path('books/<int:id>/delete/', delete_book, name='delete_book'),
    path('authors/', authors, name='authors'),
    path('create_author/', create_author, name='create_author'),
    path('authors/<int:id>/update/', update_author, name='update_author'),
    path('authors/<int:id>/delete/', delete_author, name='delete_author'),
    path('orders/', orders, name='orders'),
    path('orders/<int:id>/delete/', delete_order, name='delete_order'),
]