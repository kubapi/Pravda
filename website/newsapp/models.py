from django.db import models

#FAQs
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=600)

    def __str__(self):
        return self.question

#Category for Article
class Category(models.Model):
    title = models.CharField(max_length=50, unique = True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    
#Articles
class Article(models.Model):
    title = models.CharField(max_length=200, unique = True)
    content = models.TextField()
    short_text = models.CharField(max_length=400)

    categories = models.ManyToManyField(Category)

    published_on = models.DateTimeField()
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
