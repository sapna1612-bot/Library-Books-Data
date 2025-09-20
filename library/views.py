from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Borrow, Member
from django.utils import timezone

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available:
        member = Member.objects.first()
        Borrow.objects.create(book=book, member=member, borrow_date=timezone.now())
        book.available = False
        book.save()
    return redirect('book_list')

def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id)
    borrow.return_date = timezone.now()
    borrow.save()
    borrow.book.available = True
    borrow.book.save()
    return redirect('book_list')
