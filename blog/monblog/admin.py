from django.contrib import admin

# Register your models here.
from monblog.models import Post, Auteur

admin.site.register(Post)
admin.site.register(Auteur)