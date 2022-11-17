from django import forms

# Create your forms here.
class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
