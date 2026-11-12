
from django.db import models
from datetime import datetime


class Author(models.Model):
    name_author = models.CharField(max_length=100)
    book = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)


class Books(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    caption = models.TextField()
    due_date = models.DateField()
    picture = models.ImageField(upload_to='images/')
    quantity = models.IntegerField(default=1)
    available = models.IntegerField(default=1)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)


class Orders(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    order_number = models.IntegerField()
    books_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    days = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now)
