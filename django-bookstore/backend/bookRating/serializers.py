from rest_framework import serializers
from books.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['rating', 'user', 'book']

 
#    def create(self, validated_data):
#        comments = Comments.objects.create_comment(validated_data['rating'], validated_data['user'], validated_data['book'])
#
#        return comments

#class CommentForm(forms.ModelForm): 
#    class Meta:
#        model = Comments
#        fields = ['body']
