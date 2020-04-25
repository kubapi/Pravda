from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Article, FAQ
# from .forms import FAQForm

class FAQListView(ListView):
    model = FAQ
    template_name = 'faq_list.html'
    ordering = ['?']

def index(request):
    return render(request, 'newsapp/index.html')


# Plain views
def about(request):
    return render(request, 'newsapp/about.html')

def contact(request):
    return render(request, 'newsapp/contact.html')

def extension(request):
    return render(request, 'newsapp/extension.html')

def finances(request):
    return render(request, 'newsapp/finances.html')

def support(request):
    return render(request, 'newsapp/support.html')

def voluntary_service(request):
    return render(request, 'newsapp/voluntary-service.html')
