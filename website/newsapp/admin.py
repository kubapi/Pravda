from django.contrib import admin
from .models import Category, News, FAQ, Claim, Author, Report, Request

# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(News)
admin.site.register(Claim)
admin.site.register(FAQ)
admin.site.register(Report)
admin.site.register(Request)
