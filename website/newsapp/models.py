from django.db import models

#FAQs
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=600)

    def __str__(self):
        return self.title

#Articles
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_text = models.CharField(max_length=400)
    categories = models.ManyToManyField(Category)


    published_on = models.DateTimeField()
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
