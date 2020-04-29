from django.shortcuts import render
from django.views.generic import ListView, FormView

from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import News, FAQ, Request
from .forms import RequestForm

from .utils import grouped, translate

def index(request):
    return render(request, 'newsapp/index.html')

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
        form.save()
        return super().form_valid(form)

def archive(request):
    ctx = {}
    #captures GET parameter that we're going to send
    url_parameter = request.GET.get("q")

    if url_parameter:
        news_archives = News.objects.filter(title__icontains=url_parameter).order_by('-pub_date')
    else:
        news_archives = News.objects.all().order_by('-pub_date')

    ctx["news_archives"] = news_archives

    if request.is_ajax():
        html = render_to_string(
            template_name="news-archives-results-partial.html",
            context = {"news_archives" : news_archives}
        )
        data_dict = {"html_from_view":html}

        return JsonResponse(data=data_dict, safe = False)

    return render(request, "newsapp/archive.html", context = ctx)



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
