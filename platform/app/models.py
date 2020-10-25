# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

    pub_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']

class Claim(models.Model):
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content

class Site(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField()

    WEBSITE = 'WEB'
    FACEBOOK_PAGE = 'FBP'
    FACEBOOK_ACCOUNT = 'FBA'
    TWITTER = 'TWTRA'
    OTHER  = 'O'

    CATEGORY_CHOICES = (
        (WEBSITE, "Website (common)"),
        (FACEBOOK_PAGE,  "Facebook Page"),
        (FACEBOOK_ACCOUNT, "Facebook Account"),
        (TWITTER, "Twitter Account"),
        (OTHER, "Other"),
    )

    category = models.CharField(max_length=40, choices = CATEGORY_CHOICES, default = WEBSITE)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    number_of_published = models.IntegerField(max_length=200)

    def __str__(self):
        return self.name