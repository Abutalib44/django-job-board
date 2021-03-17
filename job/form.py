from django import forms
from .models import apply







class ApplyForm(forms.ModelForm):
    class Meta:
        model =apply
        fields=['name','email','website','cv','cover_letter']