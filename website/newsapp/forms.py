from django import forms
from .models import News, Claim, Category, News, Report, Request

class RequestForm(forms.ModelForm):

    class Meta():
        model = Request
        fields = '__all__'
