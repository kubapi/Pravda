from django.db import models

from .utils import translate

# FAQs
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=600)

    def __str__(self):
        return self.question

# Knowledge graphs
class Claim(models.Model):
    # Full claim
    text_claim = models.CharField(max_length=200, unique=True)

    # Triplets
    subject = models.CharField(max_length=40)
    predicate = models.CharField(max_length=40)
    object = models.CharField(max_length=40)

    # Verdict decides whether connection is true or false
    verdict = models.BooleanField()

    def __str__(self):
        return self.text_claim

    @property
    def get_semantic_triplet(self):
        return([self.subject, self.predicate, self.object])

    @property
    def get_translated_triplet(self):
        return translate(self.get_semantic_triplet)

# Category for Article
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

class Author(models.Model):
    pass

# Abstract class to inherit common properties
class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()

    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

# News
class News(Article):
    categories = models.ManyToManyField(Category)
    claims = models.ManyToManyField(Claim)

    # author = models.ForeignKey(Author, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "News"


class Report(Article):
    short_text = models.CharField(max_length=250)

#Given by user in form or from browser extension
class Request(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    content = models.TextField()

    SOURCE_CHOICES = [
        ('EX', 'Browser extension'),
        ('CF', 'Contact form'),
    ]
    source = models.CharField(max_length=200, choices = SOURCE_CHOICES)

    INFO_TYPE_CHOICES = [
        ('FC', 'Fact checking'),
        ('FDB', 'Feedback'),
        ('D', 'Donation'),
        ('ME', 'Media enquiry'),
        ('DE', 'Different enquiry'),
    ]
    #Used when managing special type of requests
    info_type = models.CharField(max_length=100,choices = INFO_TYPE_CHOICES)

    #If applicable
    url = models.TextField(blank=True)

    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
