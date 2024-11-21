from rest_framework import serializers
from .models import Account, Post, PostFeed, Comment

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFeed
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'