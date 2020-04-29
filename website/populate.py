# #Fake populating %TestOnly
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','website.settings')

import django
django.setup()

import random
from newsapp.models import (News, FAQ, Claim, Category, Report, Request)
from faker import Faker

fakegen = Faker()

def try_until_N(func ,N):
    iter = N
    while iter:
        try:
            func()
        except Exception as e:
            print("Something when wrong!")
            print(e)
            iter +=1
        iter -= 1

def random_paragraph(N):
    p = ''
    paragraphs = fakegen.paragraphs(nb = N)
    for e, paragraph in enumerate(paragraphs):
        if e:
            # if no 0th element
            p += " "
        p += paragraph
    return p

def random_word(capitilize = False):
    if capitilize:
        return random.choice(fakegen.sentence()[:-1].split()).capitalize()
    return random.choice(fakegen.sentence()[:-1].split())

def create_category():
    c = Category.objects.get_or_create(title=random_word(capitilize=True))[0]
    c.save()

def add_category():
    return random.choice(Category.objects.all())

def add_claim():
    c = Claim.objects.get_or_create(text_claim=fakegen.sentence()[:-1],
                                    subject = random_word().lower(),
                                    predicate = random_word().lower(),
                                    object = random_word().lower(),
                                    verdict = random.choice([0,1]))[0]
    c.save()
    return c

def populate_report():
    r = Report.objects.get_or_create(title = fakegen.sentence()[:-1],
                                     content = random_paragraph(15),
                                     short_text =random_paragraph(2))[0]

def populate_faq():
    f = FAQ.objects.get_or_create(question = fakegen.sentence()[:-1]+"?",
                                  answer = random_paragraph(3))[0]

SOURCE_CHOICES = ['EX', 'CF']
INFO_TYPE_CHOICES = ['FC', 'FDB', 'D', 'ME', 'DE']
def populate_request():
    r = Request.objects.get_or_create(email = fakegen.company_email(),
                                     subject = random_word(capitilize = True),
                                     content = random_paragraph(5),
                                     source = random.choice(SOURCE_CHOICES),
                                     info_type = random.choice(INFO_TYPE_CHOICES),
                                     url = fakegen.url())[0]

def populate_news():
    n = News.objects.get_or_create(title = fakegen.sentence()[:-1],
                                   content = random_paragraph(5))[0]

    n.categories.add(add_category())
    n.claims.add(add_claim())

    n.save()


if __name__ == '__main__':
    if input("Reset&Create categories? ") == '1':
        Category.objects.all().delete()
        try_until_N(create_category, 30)

    if input("Populate databases? ") == '1':
        print("Populating!")
        try_until_N(populate_news, 50)
        """
        ...
        ...
        ...
        """
        print("Populating completed!")
