from django.contrib import admin
from .models import Book, Member, Borrow

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn", "available")
    search_fields = ("title", "author", "isbn")
    list_filter = ("available",)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "join_date")
    search_fields = ("name", "email")

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ("book", "member", "borrow_date", "return_date")
    list_filter = ("borrow_date", "return_date")
    search_fields = ("book__title", "member__name")
