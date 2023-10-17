from django.contrib import admin

# Register your models here.
from .models import*
# admin.site.register(Book)
# from .models import Book

@admin.register(Book)
class RamAdmin(admin.ModelAdmin):
    list_display=['title','author','publication_year']