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
        
class ListPostFeedSerializer(serializers.ModelSerializer):
    account = serializers.ReadOnlyField(source = 'account.name')
    post = serializers.SerializerMethodField()
    class Mete:
        model = PostFeed
        fields = ['account', 'post']
    def get_post(self,obj):
        return obj.get.post_display

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class PostFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFeed
        fields = '__all__'