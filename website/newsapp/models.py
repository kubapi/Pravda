from django.db import models

from .utils import translate

#FAQs
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=600)

    def __str__(self):
        return self.question

#Knowledge graphs
class Claim(models.Model):
    #Full claim
    text_claim = models.CharField(max_length=200, unique = True)

    #Triplets
    subject = models.CharField(max_length=40)
    predicate = models.CharField(max_length=40)
    object = models.CharField(max_length=40)

    #Verdict decides whether connection is true or false
    verdict = models.BooleanField()



    def __str__(self):
        return self.claim

    @property
    def get_semantic_triplet(self):
        return([self.subject, self.predicate, self.object])

    @property
    def get_translated_triplet(self):
        return translate(self.get_semantic_triplet)

#Category for Article
class Category(models.Model):
    title = models.CharField(max_length=50, unique = True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


#Abstract class to inherit common properties
class Author(models.Model):
    pass

class Article(models.Model):
    title = models.CharField(max_length=200, unique = True)
    content = models.TextField()

    # pub_author = models.ForeignKey(Author)
    pub_date = models.DateTimeField()
    last_modification_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract= True


#News
class News(Article):
    categories = models.ManyToManyField(Category)
    claims = models.ForeignKey(Claim, on_delete = models.PROTECT)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
