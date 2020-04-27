from django import forms
from .models import News, Claim, Category, News, Report, Request

class ClaimForm(forms.ModelForm):
    class Meta():
        model = Claim
        fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta():
        model = News
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta():
        model = Report
        fields = '__all__'

class RequestForm(forms.ModelForm):
    class Meta():
        model = Request
        fields = '__all__'

        
