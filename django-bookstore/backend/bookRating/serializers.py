from rest_framework import serializers
from books.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['book', 'user', 'body', 'date', 'rating']

 
#    def create(self, validated_data):
#        comments = Comment.objects.create_comment(validated_data['rating'], validated_data['user'], validated_data['book'])

#        return comments

#class CommentForm(forms.ModelForm): 
#    class Meta:
#        model = Comments
#        fields = ['body']

