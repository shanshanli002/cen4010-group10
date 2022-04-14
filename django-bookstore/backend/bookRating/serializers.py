from rest_framework import serializers
from bookRating.models import Comment
from django.db.models import Avg


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'book', 'score', 'title', 'content', 'timestamp')

 

class CommentAverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'book', 'score', 'title', 'content', 'timestamp']


    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, ob):
        # reverse lookup on Reviews using item field
        return ob.Comment.all().aggregate(Avg('score'))['score__avg']