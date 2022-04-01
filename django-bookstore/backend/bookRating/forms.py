from django import forms
from .models import Comment
from .models import Comments, Books

#---------------------------------------------------------------------------------------------
class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
#---------------------------------------------------------------------------------------------

#class NewCommentForm(form.ModelForm):
#    class Meta:
#        model = Comment
#        fields = ("rating","name", "content")
#        widgets = {
#            "rating" : forms.TextInput(attrs={"class": "col-sm-12"}),
#            "name" : forms.TextInput(attrs={"class": "col-sm-12"}),
#            "content" : forms.TextInput(attrs={"class": "form-control"}),
#        }