from django.shortcuts import render
from django.views.generic import ListView, FormView


from .models import Article, FAQ, Request
from .forms import RequestForm

from .utils import grouped, translate

class FAQListView(ListView):
    model = FAQ
    template_name = 'newsapp/faq.html'

    def get_context_data(self, **kwargs):
        context = super(FAQListView, self).get_context_data(**kwargs)
        context['faq_list'] = grouped(FAQ.objects.all(), 3)
        return context

class ContactView(FormView):
    form_class = RequestForm
    template_name = 'newsapp/contact.html'

    success_url = '/kontakt/'

    def form_valid(self, form):
        print("Reached!")
        form.save()
        return super().form_valid(form)


def index(request):
    return render(request, 'newsapp/index.html')

# Plain views
def about(request):
    return render(request, 'newsapp/about.html')

def extension(request):
    return render(request, 'newsapp/extension.html')

def finances(request):
    return render(request, 'newsapp/finances.html')

def support(request):
    return render(request, 'newsapp/support.html')

def voluntary_service(request):
    return render(request, 'newsapp/voluntary-service.html')
