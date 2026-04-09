from django import forms
from .models import Books


class Books_form(forms.Form):
    Books = forms.ModelChoiceField(queryset=Books.objects.all(),label='select book')