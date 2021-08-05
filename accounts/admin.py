from django.contrib import admin

# Register your models here.

from .models import BookInformation

admin.site.register(BookInformation)