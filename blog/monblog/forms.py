from django import forms

class PostForm(forms.Form):
    titre = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)