from django import forms
from django.forms import Form

languages = [(1,"python")]
languages = [(1,"python")]

class CodeExecutorForm(Form):
<<<<<<< HEAD
    code = forms.CharField(widget=forms.Textarea,label='Code')
=======
    code = forms.CharField(widget=forms.Textarea,label='Code')
>>>>>>> decd6be466d61e303468e914f147d596a1b37162
