from django import forms
from .models import Beliefs


class PostForm(forms.ModelForm):

    class Meta:
        model = Beliefs
        fields = ('title', 'text',)
