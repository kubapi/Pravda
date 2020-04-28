# #Fake populating %TestOnly
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newsapp.settings')

import django
django.setup()

import random
from newsapp.models import (News, FAQ, Claim, Category, Report, Request)
from faker import Faker

fakegen = Faker()

# Decorator for trying N times
def try_decorator(func):

    def func_wrapper(*args, **kwargs):
        try:
           return func(*args, **kwargs)

        except Exception as e:

            print(e)
            return None

    return func_wrapper




def test_decorator(arg1):

    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print "Congratulations.  You decorated a function that does something with %s and %s" % (arg1, arg2)
            function(*args, **kwargs)
        return wrapper

    return real_decorator


@decorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print arg







def random_word():
    return random.choice(fakegen.sentence().split())

def add_category():
    #in case of "unique" problem
    while True:
        try:
            c = Category.objects.get_or_create(title=random_word())[0]
            c.save()
            return c

def add_claim():
    while True:
        try:
            c = Category.objects.get_or_create(text_claim=fakegen.sentence(),
                                               subject = random_word(),
                                               predicate = random_word(),
                                               object = random.word(),
                                               verdict = fakegen.pybool())[0]
            c.save()
            return c

def populate_news(*N=40):
    for _ in range(N):
        while True:
            try:
                n


def populate_faq(*N=12):
def populate_report(*N=15):
def populate_request(*N=200):


if __name__ == '__main__':
    if input("Delete all previous records?") == 1:
        News.objects.all().delete()
        FAQ.objects.all().delete()
        Category.objects.all().delete()
        Claim.objects.all().delete()
        Report.objects.all().delete()
        Request.objects.all().delete()

    if input("Populate databases?") == 1:
        populate_news()
        populate_faq()
        populate_report()
        populate_request()
