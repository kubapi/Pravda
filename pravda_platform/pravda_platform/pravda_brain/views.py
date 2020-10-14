from django.shortcuts import render


def index(request):
    return render(request, 'pravda_brain/index.html')

