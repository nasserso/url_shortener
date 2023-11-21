from django.contrib import admin
from shortener.models import Shortener


@admin.register(Shortener)
class AuthorAdmin(admin.ModelAdmin):
    pass
