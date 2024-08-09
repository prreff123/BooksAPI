from rest_framework import serializers
from .models import Book,Recommendation,Like,Comment

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Recommendation
        fields = ['id', 'user', 'book', 'comment', 'created_at', 'likes_count', 'comments_count']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'        