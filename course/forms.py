from django import forms
from .models import Info


class InfoForm(forms.ModelForm):
    
    class Meta:
        model = Info
        fields = ['first_name', 'last_name', 'email', 'course_id', 'enquiry', 'recommendation']