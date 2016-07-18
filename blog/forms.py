from django import forms
from .models import Beliefs

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class PostForm(forms.ModelForm):

    class Meta:
        model = Beliefs
        fields = ('title', 'text',)
        
