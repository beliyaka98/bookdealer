from django import forms

class SearchForm(forms.Form):
    book_name = forms.CharField(label='Book name', max_length=100, required=False)