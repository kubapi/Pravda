# -*- encoding: utf-8 -*-

from django.contrib import admin

from .models import Author, Article, Claim, Site

# Register your models here.
admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Claim)
admin.site.register(Site)



