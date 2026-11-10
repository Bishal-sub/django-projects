from django import forms
from .models import expense_model


class expense_model_Form(forms.ModelForm):
    
    class Meta:
        model = expense_model
        fields = ("category","name","description","amount")
        
