from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.models import User

class NewMessageForm(forms.Form):
    user_to = forms.ModelChoiceField(label='To:', queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'mb-2 form-control form-select'}))
    message = forms.CharField(label='Message:', widget=forms.Textarea(attrs={'class':'form-control', "rows": 15}))