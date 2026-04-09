from django.contrib import admin
from .models import Gif

# Register your models here.

@admin.register(Gif)
class GifAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'description')