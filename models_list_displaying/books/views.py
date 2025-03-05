import datetime
from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    list_book = Book.objects.all()
    context = {
        'list_book': list_book,
        }
    return render(request, template, context)

def date_view(request, pub_date):
    template = 'books/index.html'
    pub_date = datetime.date.strftime(pub_date,'%Y-%m-%d')
    books_pub = Book.objects.filter(pub_date=pub_date)
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    prev_date = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').last()
    if next_date:
        next_date = str(next_date.pub_date)
    else:
        next_date = ''
    if prev_date:
        prev_date = str(prev_date.pub_date)
    else:
        prev_date = ''
    context = {
        'books_pub': books_pub,
        'next_date': next_date,
        'prev_date': prev_date,
    }
    return render(request, template, context)