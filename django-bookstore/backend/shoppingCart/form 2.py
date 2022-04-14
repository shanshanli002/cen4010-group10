from django import forms
from books.models import Book

class shoppingCartForm(forms.Form):
    book_pk = forms.IntegerField(min_value=1)
    next_link = forms.CharField(max_length=240)
   